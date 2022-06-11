class solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countlist = []
        checklist = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1] and s[i] not in checklist:
                checklist.append(s[i])
                countlist.append(len(checklist))
            elif s[i] == s[i - 1]:
                countlist.append(len(checklist))
                checklist.clear()
                checklist.append(s[i])

        return max(countlist)


a = solution()
print(a.lengthOfLongestSubstring('absabsabs'))
print(a.lengthOfLongestSubstring('bbbbbb'))
print(a.lengthOfLongestSubstring('pwwkew'))