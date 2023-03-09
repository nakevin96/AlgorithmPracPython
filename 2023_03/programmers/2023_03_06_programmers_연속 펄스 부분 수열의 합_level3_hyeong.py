# https://school.programmers.co.kr/learn/courses/30/lessons/161988

# 처음 풀이 - 못 품
def solution(sequence):
    result = sum(sequence)
    total = result
    max_idx = 0
    max_val = 0
    for idx, val in enumerate(sequence):
        if abs(val) > max_val:
            max_idx, max_val = idx, abs(val)
    
    left, right = max_idx, max_idx
    
    if sequence[max_idx] < 0:
        # 제일 큰 값이 음수일때부터
        c_left, c_right = 1, 1
        while left != 0 or right != len(sequence) - 1:
            if left > 0:
                left -= 1
                if c_left == 1:
                    total = total - sequence[left] + (sequence[left] * c_left)
                    c_left *= -1
                else:
                    total = total - sequence[left] + (sequence[left] * c_left)
                    c_left *= -1
                result = max(result, total)
                
            if right < len(sequence) - 2:
                right += 1
                if c_right == 1:
                    total = total - sequence[right] + (sequence[right] * c_right)
                    c_right *= -1
                else:
                    total = total - sequence[right] + (sequence[right] * c_right)
                    c_right *= -1
                result = max(result, total)
    else:
        c_left, c_right = -1, -1
        while left != 0 or right != len(sequence) - 1:
            if left > 0:
                left -= 1
                if c_left == 1:
                    total = total - sequence[left] + (sequence[left] * c_left)
                    c_left *= -1
                else:
                    total = total - sequence[left] + (sequence[left] * c_left)
                    c_left *= -1
                result = max(result, total)
                
            if right < len(sequence) - 2:
                right += 1
                if c_right == 1:
                    total = total - sequence[right] + (sequence[right] * c_right)
                    c_right *= -1
                else:
                    total = total - sequence[right] + (sequence[right] * c_right)
                    c_right *= -1
                result = max(result, total)
        
    return result


# 두 번째 풀이
def solution(sequence):
    dp1 = [0] * len(sequence)
    dp2 = dp1[::]
    
    dp1[0] = sequence[0]
    dp2[0] = -sequence[0]
    
    for i in range(1, len(sequence)):
        dp1[i] = max(dp2[i-1]+sequence[i], sequence[i])
        dp2[i] = max(dp1[i-1]-sequence[i], -sequence[i])
    
    return max(max(dp1), max(dp2))