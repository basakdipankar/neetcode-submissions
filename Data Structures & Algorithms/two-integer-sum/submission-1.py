class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        for i, n in enumerate(nums):
            if i == 0:
                nums_idx[n] = i
                continue
            if (target - n) in nums_idx and nums_idx[target-n] != i:
                return [nums_idx[target-n], i]
            nums_idx[n] = i