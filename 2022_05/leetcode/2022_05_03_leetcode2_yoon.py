# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_list = []
        num2_list = []
        while l1 != None:
            num1_list.append(l1.val)
            l1 = l1.next

        while l2 != None:
            num2_list.append(l2.val)
            l2 = l2.next

        # int형 list는 join을 사용할 수 없어 map을 사용해 int를 str로 변경
        num1_origin = int(''.join(map(str, reversed(num1_list))))
        num2_origin = int(''.join(map(str, reversed(num2_list))))

        result_num_list = list(str(num1_origin + num2_origin))[::-1]

        start_node = ListNode()
        next_node = start_node
        for i in range(len(result_num_list)):
            if i == 0:
                next_node.val = result_num_list[0]
            else:
                tmp_node = ListNode()
                tmp_node.val = result_num_list[i]
                next_node.next = tmp_node
                next_node = tmp_node

        return start_node


