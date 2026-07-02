class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # We can easily solve this problem using either a dictionary or a set data structure
        # This solution will be of O(n) space and time complexity
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
        