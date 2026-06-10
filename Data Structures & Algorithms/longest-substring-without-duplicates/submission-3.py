class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        left = 0
        max_sub = 0
        for right in range(len(s)):
            while s[right] in s_set:
                s_set.remove(s[left])
                left += 1
            s_set.add(s[right])
            max_sub = max(max_sub, right - left + 1)
        return max_sub