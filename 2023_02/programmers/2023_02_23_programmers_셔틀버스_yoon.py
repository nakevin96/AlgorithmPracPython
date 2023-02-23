def solution(n, t, m, timetable):
    minute_timetable_len = len(timetable)
    minute_timetable = []
    # 셔틀이 도착하는 시간을 분으로 표현
    arrival_time = [540 + (t * i) for i in range(n)]
    # 셔틀에 탑승하는 고객이 어느 시간에 도착하는지 기록
    boarding_list = [[] for _ in range(n)]

    # time table의 시: 분 정보를 분으로 변경
    for t in timetable:
        [hour, minute] = t.split(":")
        minute_timetable.append(int(hour) * 60 + int(minute))

    # 먼저 온 크루부터 확인하기 위해 sorting
    minute_timetable.sort()
    mt_idx = 0

    # 셔틀 도착 시간과 크루 도착시간을 순회하며 셔틀 도착 전에 기다리고 있던 크루를 한명씩 태움(boarding_list)
    for ai, at in enumerate(arrival_time):
        boarding_count = 0
        # 크루가 셔틀 도착시간 이전에 왔고, 아직 셔틀이 가득차지 않앗다면 탑승
        while mt_idx < minute_timetable_len and minute_timetable[mt_idx] <= at and boarding_count < m:
            boarding_list[ai].append(minute_timetable[mt_idx])
            boarding_count += 1
            mt_idx += 1

    # 기본적으로 가장 늦게 도착가능한 시간은 버스 마지막 도착시간
    my_arrival_time = arrival_time[-1]

    # 마지막 버스 가득 찼다면 그 버스 마지막 탑승자보다 1분만 먼저 도착하면 됌.
    if len(boarding_list[-1]) >= m:
        my_arrival_time = boarding_list[-1][-1] - 1

        # hh: mm형태로 맞춰주기 위해 앞에 '0'붙여서 자름
    my_hour, my_minute = '0' + str(my_arrival_time // 60), '0' + str(my_arrival_time % 60)
    return f'{my_hour[-2:]}:{my_minute[-2:]}'

# javascript로 풀어본것
# function solution(n, t, m, timetable) {
#     const getTimeResult = (time)=>{
#         const [hour, minute] = ['00'+parseInt(time/60), '00'+time%60]
#         return `${hour.slice(-2)}:${minute.slice(-2)}`;
#     };
#     const baseTime = 540;
#     const arrivalTimes = [];
#     for(let i=0; i<n; i++){
#         arrivalTimes.push(baseTime+(t*i));
#     }
#     timetable = timetable.map((timeString)=>{
#         const timeArray = timeString.split(':');
#         const [hour, minute] = [Number(timeArray[0]), Number(timeArray[1])];
#         return hour*60 + minute;
#     });
#     timetable.sort((a,b)=>a-b);
#     const queue = Array.from({length:n},()=>Array.from({length:0}));
#     let arrivalIdx = 0;
#     let isOver = false;
#     for(const time of timetable){
#         if(isOver){
#             continue;
#         }
#         while((arrivalIdx < arrivalTimes.length) && (time>arrivalTimes[arrivalIdx] || queue[arrivalIdx].length >= m)){
#             arrivalIdx++;
#         }
#         if(arrivalIdx === arrivalTimes.length){
#             isOver = true;
#             continue;
#         }
#         queue[arrivalIdx].push(time);
#     }
#     if(queue.at(-1).length < m){
#         return getTimeResult(arrivalTimes.at(-1))
#     }else{
#         return getTimeResult(queue.at(-1).at(-1)-1)
#     }
# }