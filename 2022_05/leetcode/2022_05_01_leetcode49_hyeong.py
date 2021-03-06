import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strdic = {}
        # for i in strs:
        #     if "".join(sorted(i)) in strdic:
        #         strdic["".join(sorted(i))] += [i]
        #     else:
        #         strdic["".join(sorted(i))] = [i]
        # return strdic.values()

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

a = Solution.groupAnagrams(input_list)
