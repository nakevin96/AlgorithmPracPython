#첫 풀이 타임에러 나서 안됌
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s
#
#         result = ""
#         for check_len in range(len(s), 0, -1):
#             for start_idx in range(len(s) - check_len + 1):
#                 test_str = s[start_idx:start_idx + check_len]
#                 is_pal = True
#                 check_idx_range = check_len // 2
#                 for check_idx in range(check_idx_range):
#                     if test_str[check_idx] != test_str[-(check_idx + 1)]:
#                         is_pal = False
#                         break
#                 if is_pal and check_len > len(result):
#                     result = test_str
#                     return result
#
#         return result
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getMaxPal(mid1, mid2):
            max_pal = s[mid1]
            if s[mid1] != s[mid2]:
                return s[mid1]
            else:
                max_pal = s[mid1:mid2 + 1]

            left, right = mid1 - 1, mid2 + 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    max_pal = s[left:right + 1]
                    left = left - 1
                    right = right + 1
            return max_pal

        if len(s) < 2:
            return s
        if len(set(s)) == len(s):
            return s[0]
        if s == s[::-1]:
            return s

        result = ""
        for mid_idx in range(len(s) - 1):
            tmp_max_pal1 = getMaxPal(mid_idx, mid_idx)
            tmp_max_pal2 = getMaxPal(mid_idx, mid_idx + 1)
            result = max(result, tmp_max_pal1, tmp_max_pal2, key=len)

        return result