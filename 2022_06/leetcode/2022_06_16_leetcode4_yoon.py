from collections import deque


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums1_len + nums2_len == 0:
            return 0

        d_nums1 = deque(nums1)
        d_nums2 = deque(nums2)
        mid_point_idx = (nums1_len + nums2_len + 1) // 2
        count = 0

        mid_value = 0

        while True:
            if count == mid_point_idx:
                break

            if d_nums1 and d_nums2:
                if d_nums1[0] <= d_nums2[0]:
                    mid_value = d_nums1.popleft()
                    count += 1
                else:
                    mid_value = d_nums2.popleft()
                    count += 1
            elif d_nums1:
                mid_value = d_nums1.popleft()
                count += 1
            else:
                mid_value = d_nums2.popleft()
                count += 1

        if (nums1_len + nums2_len) % 2 == 1:
            return mid_value
        else:
            if d_nums1 and d_nums2:
                mid_value2 = min(d_nums1[0], d_nums2[0])
                return (mid_value + mid_value2) / 2
            elif d_nums1:
                return (mid_value + d_nums1[0]) / 2
            else:
                return (mid_value + d_nums2[0]) / 2

