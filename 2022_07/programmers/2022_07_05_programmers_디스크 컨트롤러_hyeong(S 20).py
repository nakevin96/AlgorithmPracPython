import heapq

def solution(jobs):
    start, end, i, result = -1, 0, 0, 0
    heap = list()

    while i < len(jobs):  # i -> 작업 수행 count :: 즉 i가 하나씩 증가하며 작업 길이와 같아지면 끝
        for job in jobs:  # 작업을 모두 검사하며 start 시간과 end 시간 사이에 있는 작업을 heapq에 추가
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])  # 반대로 저장하는 이유는 소요시간이 작은것 부터 구하려고(최소힙)

        if 0 < len(heap):  # heap list에 작업이 존재한다면
            temp = heapq.heappop(heap)
            start = end
            end += temp[0]
            result += end - temp[1]  # result는 총 작업 시간 :: end -> 작업이 끝난 시간에서 작업이 요청된 시간을 빼면 대기시간이 나옴
            i += 1  # 작업이 한 개 수행되었으므로 수행
        else:  # 사이에 작업이 없으면 하나씩 end를 늘려서 사이에 들어오는 작업 수행
            end += 1

    return result // len(jobs)