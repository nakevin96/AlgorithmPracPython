# leetcode에서 동작시킨 코드
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for num in nums:
#             num_idx = nums.index(num)
#             num_remain = target - num
#
#             if num_remain in nums[num_idx + 1:]:
#                 return [num_idx, nums[num_idx + 1:].index(num_remain) + num_idx + 1]
#         return None

def two_sum(nums, target):
    for num in nums:
        num_idx = nums.index(num)
        num_remain = target - num

        if num_remain in nums[num_idx + 1:]:
            return [num_idx, nums[num_idx + 1:].index(num_remain) + num_idx + 1]

    return None
