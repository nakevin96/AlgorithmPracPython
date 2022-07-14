from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tic_list = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            tic_list[a].append(b)

        result_list = list()
        def dfs(val):
            while tic_list[val]:
                dfs(tic_list[val].pop())
            result_list.append(val)
        dfs("JFK")
        return result_list[::-1]