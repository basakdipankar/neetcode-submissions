class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i, n in enumerate(nums):
            left = i+1
            right = len(nums) -1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum == 0:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    right -= 1
        return list(result)