"""
leetcode에서 동작시킨 코드

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in sorted_strs:
                sorted_strs[sorted_word] = [word]
            else:
                sorted_strs[sorted_word].append(word)

        return sorted_strs.values()
"""

