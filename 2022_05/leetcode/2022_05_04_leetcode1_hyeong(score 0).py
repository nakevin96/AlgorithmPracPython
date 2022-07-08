# # 첫 번째 방식
# #python 스럽지 않은 노가다 방식... 상위 95% 속도...
# def fun1(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if (nums[i] + nums[j]) == target:
#                 return [i, j]

# # 두 번째 방식 enumerate 사용
# # 제일 빠르고 좋음
# # 대가리 터질것 같음 ㅜㅜ
def fun2(nums, target):
    nums_dict = dict()
    for key, val in enumerate(nums):
        if target - val in nums_dict:
            return [nums_dict[target - val], key]
        else:
            nums_dict[val] = key

num_list = [2, 7, 11, 15]
target_num = 9

# print(fun1(num_list, target_num))
print(fun2(num_list, target_num))