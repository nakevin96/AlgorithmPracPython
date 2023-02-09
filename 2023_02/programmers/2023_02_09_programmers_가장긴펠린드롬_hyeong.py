# https://school.programmers.co.kr/learn/courses/30/lessons/12904?language=python3

# 첫 번째 풀이 실패
def solution(s):
    result = 0
    def palin(index):
        temp = 1
        left, right = index-1, index+1
        if left < 0 or right >= len(s):
            return temp
        while s[left] == s[right]:
            left -= 1
            right += 1
            temp += 2
            if left < 0 or right >= len(s):
                return temp
        return temp
    
    for i in range(len(s)):
        result = max(result, palin(i))
        if result == len(s):
            return result
    
    return result

# 두 번째 풀이 성공
def solution(s):
    result = 0
    
    def palin(left, right):
        temp = 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            temp += 2
        return temp
    
    def palin2(left, right):
        temp = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            temp += 2
        return temp
    
    for i in range(len(s)):
        result = max(result, palin(i-1, i+1), palin2(i, i+1))
        if result == len(s):
            return result
    
    return result