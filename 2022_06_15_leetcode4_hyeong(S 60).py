from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_list = list()
        M_val = 0
        if not nums1 and not nums2:
            return 0

        if not nums2:
            for i in nums1:
                nums2.append(i)
            sum_list = nums2
        else:
            for i in nums2:
                nums1.append(i)
            sum_list = nums1

        sum_list.sort()


        if len(sum_list) % 2 != 0:
            if len(sum_list) == 1:
                return sum_list[0]
            M_val = sum_list[len(sum_list) // 2]
        else:
            M_val = (sum_list[len(sum_list) // 2] + sum_list[len(sum_list) // 2 - 1]) / 2
        return M_val

a = Solution()
print(a.findMedianSortedArrays([1, 2], [3, 4]))
print(a.findMedianSortedArrays([1, 3], [2]))
# print(a.findMedianSortedArrays([], [22]))

