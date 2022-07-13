from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start_list = list()
        tickets = sorted(tickets, key=lambda x: x[1])
        for tic in tickets:
            if tic[0] == "JFK" and tic[1] in [x[0] for x in tickets]:
                for t in tic:
                    start_list.append(t)
                tickets.remove(tic)
                break
            elif tic[0] == "JFK" and len(tickets) == 1:
                return tickets[0]
        count = len(tickets)
        while count > 0:
            temp_list = list()
            for i in tickets:
                if start_list[-1] == i[0] and i[1] in [x[0] for x in tickets]:
                    temp_list.append(i)
                    start_list.append(temp_list[0][1])
                    tickets.remove(i)
                    count -= 1
                    break
                elif count == 1:
                    start_list.append(i[1])
                    count -= 1

        return start_list

a = Solution()
# print(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(a.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(a.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],\
                       ["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],\
                       ["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],\
                       ["EZE","ANU"],["AUA","ANU"]]))