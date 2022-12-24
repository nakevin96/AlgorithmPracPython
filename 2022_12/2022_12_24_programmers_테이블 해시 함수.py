# https://school.programmers.co.kr/learn/courses/30/lessons/147354

# 해결

def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    result = []
    for i in range(len(data)):
        data[i].append(i+1)
    temp_data = data[row_begin - 1:row_end]
    for i in temp_data:
        i_temp = 0
        for j in range(len(i) - 1):
            i_temp += (i[j] % i[-1])
        result.append(i_temp)
        
    temp = result[0]
    for i in result[1:]:
        temp = temp ^ i
    
    return tem결