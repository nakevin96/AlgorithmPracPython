from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def fun1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1_re = l1[::-1] # list 1 의 역순
        # l2_re = l2[::-1] # list 2 의 역순
        l1.reverse()
        l2.reverse()
        # l1_re = list(reversed(l1))
        # l2_re = list(reversed(l2))
        l1_sum = 0
        l2_sum = 0

        for i in range(len(l1)):
            l1_sum += (10 ** i) * l1[i]

        for i in range(len(l2)):
            l2_sum += (10 ** i) * l2[i]

        l3_sum = l1_sum + l2_sum
        l3 = []
        for i in str(l3_sum):
            l3.append(i)

        l3 = list(map(int, l3))
        l3.reverse()

        return l3


l1 = [2, 4, 3]
l2 = [5, 6, 4]
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]

a = Solution()
print(a.fun1(l1, l2))