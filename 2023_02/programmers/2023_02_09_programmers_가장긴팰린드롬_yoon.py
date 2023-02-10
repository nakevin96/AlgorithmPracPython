# 통과는 했으나 상당히 비효율적이었던 풀이방법.. for문이 너무 많이 겹침
def solution3(s):
    if len(s) == 1:
        return 1
    result = 1
    max_len = (len(s) - 1) // 2
    for base_idx in range(1, len(s)):
        for curr_len in range(min(max_len, base_idx, len(s) - base_idx - 1), 0, -1):
            is_palindrome = True
            for check_idx in range(base_idx - curr_len, base_idx):
                if s[check_idx] != s[base_idx + base_idx - check_idx]:
                    is_palindrome = False
                    break
            if is_palindrome:
                result = max(2 * curr_len + 1, result)
                break

        for check_idx in range(1, (base_idx + 1) // 2 + 1):
            if s[base_idx - check_idx] != s[base_idx + check_idx]:
                break
            result = max(2 * check_idx, result)
    return result


# 재귀 방식으로 풀이하는 방법
def solution2(s):
    def find_longest_palindrome_length(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) == 1:
        return 1
    result = 1
    for base_idx in range(len(s) - 1):
        result = max(result, find_longest_palindrome_length(base_idx, base_idx),
                     find_longest_palindrome_length(base_idx, base_idx + 1))
    return result


# manacher 알고리즘을 사용한 풀이
def solution(s):
    if len(s) == 1:
        return 1
    s = "!".join(f"!{s}!")
    s = s[1:-1]
    s_len = len(s)

    right = center = -1
    pt = [0 for _ in range(s_len)]
    for curr_idx in range(len(s)):
        # 처음부터 탐색해야 하는 상황
        if right < curr_idx:
            center = right = curr_idx
            while right < s_len and 2 * center >= right and s[right] == s[2 * center - right]:
                right += 1
            right -= 1
            pt[curr_idx] = right - center
        # 앞에서 구한 pt값 활용할 수 있는 상황
        else:
            sym_idx = 2 * center - curr_idx
            if pt[sym_idx] < right - curr_idx:
                pt[curr_idx] = pt[sym_idx]
            elif pt[sym_idx] == right - curr_idx:
                center = right = curr_idx
                while right < s_len and 2 * center >= right and s[right] == s[2 * center - right]:
                    right += 1
                right -= 1
                pt[curr_idx] = right - center
            else:
                pt[curr_idx] = right - curr_idx

    return max(pt)
