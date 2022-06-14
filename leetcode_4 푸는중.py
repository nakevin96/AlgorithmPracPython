from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_dict = {}
        for key, val in enumerate(nums1):
            num_dict[key] = val
        for i in nums2:
            for j in range(len(nums2)):
                if i <= num_dict[j]:
                    pass

        return num_dict

a =Solution()
print(a.findMedianSortedArrays([1, 3], [2]))

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000