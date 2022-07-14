from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        ticket_dict = defaultdict(list)
        for ticket in sorted(tickets, reverse=True):
            ticket_dict[ticket[0]].append(ticket[1])

        stack = ["JFK"]

        while stack:
            while ticket_dict[stack[-1]]:
                stack.append(ticket_dict[stack[-1]].pop())
            result.append(stack.pop())

        return reversed(result)