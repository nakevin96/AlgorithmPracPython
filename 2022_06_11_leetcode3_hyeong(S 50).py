class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        countlist = [1]
        checklist = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1] and s[i] not in checklist:
                checklist.append(s[i])
                countlist.append(len(checklist))
            elif s[i] == s[i - 1]:
                countlist.append(len(checklist))
                checklist.clear()
                checklist.append(s[i])
            elif s[i] != s[i - 1] and s[i] in checklist:
                countlist.append(len(checklist))
                while True:
                    if checklist.pop(0) == s[i]:
                        break
                checklist.append(s[i])

        return max(countlist)


a = Solution()
# print(a.lengthOfLongestSubstring('abcabcbb'))
# print(a.lengthOfLongestSubstring('bbbbbb'))
# print(a.lengthOfLongestSubstring('pwwkew'))
# print(a.lengthOfLongestSubstring(' '))
# print(a.lengthOfLongestSubstring('ckilbkd'))
# print(a.lengthOfLongestSubstring('dvdf'))
print(a.lengthOfLongestSubstring('jlygy'))