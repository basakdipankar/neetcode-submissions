class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This is kadane's algorithm
        current_sum = max_sum = nums[0]
        start = end = 0
        for i in range(1, len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                start = i
            else:
                current_sum = current_sum + nums[i]
                end = i

            if current_sum > max_sum:
                max_sum = current_sum
        # print(nums[start:end+1])
        return max_sum
