class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # keep track of numbers and their indices
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i