class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        for i, n in enumerate(nums):
            if (target - n) in nums_idx:
                return [nums_idx[target-n], i]
            nums_idx[n] = i