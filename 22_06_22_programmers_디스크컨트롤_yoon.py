import heapq


def solution(jobs):
    if not jobs:
        return 0
    jobs.sort(key=lambda x: x[0])
    disk_heap = []
    start_time = 0
    check_idx = 0
    total_time = 0
    total_len = len(jobs)

    while check_idx < total_len:
        if jobs[check_idx][0] <= start_time:
            heapq.heappush(disk_heap, (jobs[check_idx][1], jobs[check_idx][0]))
            check_idx += 1
            continue

        if disk_heap:
            curr_job = heapq.heappop(disk_heap)
            total_time = total_time + start_time + curr_job[0] - curr_job[1]
            start_time = start_time + curr_job[0]
        else:
            start_time += 1

    while disk_heap:
        curr_job = heapq.heappop(disk_heap)
        total_time = total_time + start_time + curr_job[0] - curr_job[1]
        start_time = start_time + curr_job[0]

    return total_time // total_len