class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxval = 0
        s_dict = dict()
        if len(s) < 2:
            return len(s)

        for key, val in enumerate(s):
            if val in s_dict and start <= s_dict[val]:
                start = s_dict[val] + 1
            else:
                maxval = max(maxval, key - start + 1)
            s_dict[val] = key

        return maxval


a = Solution()

print(a.lengthOfLongestSubstring('tmmzuxt'))  # 5
# print(a.lengthOfLongestSubstring('abcabcbb'))  # 3
# print(a.lengthOfLongestSubstring('bbbbbb'))  # 1
# print(a.lengthOfLongestSubstring('pwwkew'))  # 3
# print(a.lengthOfLongestSubstring(' '))  # 1
# print(a.lengthOfLongestSubstring('ckilbkd'))  # 5
# print(a.lengthOfLongestSubstring('dvdf'))  # 3
# print(a.lengthOfLongestSubstring('jlygy'))  # 4
