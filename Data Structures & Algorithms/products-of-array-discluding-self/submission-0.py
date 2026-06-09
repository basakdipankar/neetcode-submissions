class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        l_product = 1
        for n in nums:
            result.append(l_product)
            l_product *= n
        r_product = 1
        for i in range(-1, -len(nums) -1, -1):
            result[i] *= r_product
            r_product *= nums[i]
        return result
