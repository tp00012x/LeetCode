# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Brute force
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

#Enumerate
# def twoSum(nums, target):
#         for i, n in enumerate(nums):
#             if target - n in nums and nums.index(target-n) != i:
#                 return sorted([i, nums.index(target - n)])

#Better solution
# def twoSum(nums, target):
#     seen = {}
#     for count, char in enumerate(nums):
#         remaining = target - char
#         if remaining in seen:
#             return [seen[remaining], count]
#         seen[char] = count
#     return []

def twoSum(nums, target):
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        buff_dict[target - nums[i]] = i

print(twoSum([2, 11, 15, 7], 9))