# 이전 작성 코드
# def solution(s):
#     if len(s) == 1:
#         return 1
#     answer = len(s)
#
#     for comp_len in range(1, (len(s) // 2) + 1):
#         idx = 0
#         comp_string = ""
#         comp_count = 1
#         comp_store = ""
#         while idx < len(s):
#             if idx + comp_len >= len(s):
#                 if s[idx:] != comp_store:
#                     if comp_count == 1:
#                         comp_string = comp_string + comp_store + s[idx:]
#                     else:
#                         comp_string = comp_string + str(comp_count) + comp_store + s[idx:]
#                 else:
#                     comp_string = comp_string + str(comp_count + 1) + comp_store
#                 break
#             if s[idx: idx + comp_len] == comp_store:
#                 comp_count += 1
#                 idx += comp_len
#             else:
#                 if comp_count == 1:
#                     comp_string += comp_store
#                 else:
#                     comp_string = comp_string + str(comp_count) + comp_store
#                 comp_count = 1
#                 comp_store = s[idx:idx + comp_len]
#                 idx += comp_len
#
#         if len(comp_string) < answer:
#             answer = len(comp_string)
#     return answer


def solution(s):
    def getCompStringLen(comp_len):
        result_len = 0
        count = 1
        for check_idx in range(0, len(s), comp_len):
            if s[check_idx:check_idx+comp_len] == s[check_idx+comp_len:check_idx+(2*comp_len)]:
                count += 1
            else:
                adder = len(str(count)) if count > 1 else 0
                result_len += (adder + len(s[check_idx:check_idx+comp_len]))
                count = 1
        return result_len
    if len(s) == 1:
        return 1
    result = 1001
    for _comp_len in range(1, (len(s)//2) +1):
        result = min(getCompStringLen(_comp_len), result)
    return result
