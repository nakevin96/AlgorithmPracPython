def solution(number, k):
    def move_idx(start, end):
        nonlocal k
        max_val = -1
        max_idx = -1
        for n in range(start, end + 1):
            if int(number[n]) > max_val:
                max_val = int(number[n])
                max_idx = n
            if max_val == total_max_val:
                break
        k = k - 1
        return str(max_val), max_idx + 1

    if len(number) == k - 1:
        return max(number)
    total_max_val = int(max(number))
    result = ""
    k = len(number) - k
    s = 0
    e = len(number) - k
    while k > 1:
        m_value, s = move_idx(s, e)
        e = len(number) - k
        result += m_value

    return result + max(number[s:])