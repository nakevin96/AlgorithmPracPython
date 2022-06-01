# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 재귀랑, 추가 함수 구현해서 만드는 방식

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            curr, prev = head, None
            while curr:
                next, curr.next = curr.next, prev
                prev, curr = curr, next
            return prev

        def listNode_to_list(head):
            result_list = []
            while head:
                result_list.append(head.val)
                head = head.next
            return result_list

        def list_to_listNode(input_list):
            result = head = ListNode()
            for item in input_list:
                head.next = ListNode(item)
                head = head.next
            return result.next

        num1 = int(''.join(map(str, listNode_to_list(reverse(l1)))))
        num2 = int(''.join(map(str, listNode_to_list(reverse(l2)))))
        num3 = num1 + num2

        return reverse(list_to_listNode(map(int, list(str(num3)))))


# 전가산기 구현하는 방식 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode()

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


# 전가산기 구현하는 방식 2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_listNode(input_list):
            result = head = ListNode()
            for item in input_list:
                head.next = ListNode(item)
                head = head.next
            return result.next

        carry = 0
        result_list = []
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            result_list.append(tmp % 10)
            carry = tmp // 10
            l1, l2 = l1.next, l2.next

        while l1:
            tmp = l1.val + carry
            result_list.append(tmp % 10)
            carry = tmp // 10
            l1 = l1.next
        while l2:
            tmp = l2.val + carry
            result_list.append(tmp % 10)
            carry = tmp // 10
            l2 = l2.next
        if carry != 0:
            result_list.append(carry)

        return list_to_listNode(result_list)