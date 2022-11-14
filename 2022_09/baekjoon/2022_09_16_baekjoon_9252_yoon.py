import sys

sys_input = sys.stdin.readline


def solution():
    str1 = sys_input().rstrip()
    str2 = sys_input().rstrip()
    str1_len = len(str1)
    str2_len = len(str2)
    dt = [["" for _s1 in range(str1_len + 1)] for _s2 in range(str2_len + 1)]

    for s2_idx in range(str2_len):
        for s1_idx in range(str1_len):
            if str1[s1_idx] == str2[s2_idx]:
                dt[s2_idx + 1][s1_idx + 1] = dt[s2_idx][s1_idx] + str1[s1_idx]
            else:
                dt[s2_idx + 1][s1_idx + 1] = max(dt[s2_idx][s1_idx + 1], dt[s2_idx + 1][s1_idx], key=len)

    result = dt[str2_len][str1_len]
    if len(result) == 0:
        print(0)
    else:
        print(len(result))
        print(result)


solution()
