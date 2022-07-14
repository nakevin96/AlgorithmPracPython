class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        while s:
            result_list = []
            for i in s[::-1]:
                result_list.append(i)
                if result_list[::] == result_list[::-1] and len(result_list) > 1:
                    return str(result_list)
            s.pop()
        return str(result_list)

a = Solution()

print(a.longestPalindrome("babad"))