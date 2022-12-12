# https://school.programmers.co.kr/learn/courses/30/lessons/142085#

# 푸는 중 -> 브루트 포스로 풀어봄
# 이분탐색으로 풀어야함 ing

from collections import deque

def solution(n, k, enemy):
    queue = deque(enemy)
    use_k_index = []
    
    for i in range(len(enemy)):
        temp = 0
        temp_list = enemy[i:]
        j = 0
        while temp < n:
            temp += enemy[j]
            j += 1
        check_shield = [(index, enemy[i:j][index]) for index in range(len(enemy[i:j]))]
        check_shield.sort(key=lambda x:x[1], reverse=True)
        use_k_index = [check_shield[x] for x in range(k)]
        for use in use_k_index:
            if use[0] == i:
                k -= 1
                break
        else:
            n -= enemy[i]
            if n < 0:
                return i
    return len(enemy)