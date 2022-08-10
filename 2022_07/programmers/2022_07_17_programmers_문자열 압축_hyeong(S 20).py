def solution2(s, cnt):
    str_list = []
    result_str = ''
    tmp = 1
    for p in range(0, len(s) + 1, cnt):
        start, end, end2 = p, p + cnt, cnt + (p + cnt)
        if s[start:end] == s[end:end2]:
            tmp += 1
        else:
            str_list.append([s[start:end], tmp])
            tmp = 1
    return ''.join([i[0] if i[1] == 1 else (str(i[1]) + i[0]) for i in str_list])

def solution(s):
    if len(s) == 1:
        return 1
    max_len = len(s) // 2
    return len(min([(solution2(s, x)) for x in range(1, max_len + 1)], key=len))


a = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", \
     "xababcdcdababcdcd", "a"]
for i in a:
    print(solution(i))
