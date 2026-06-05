class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Match length of both the strings
        if len(s) != len(t):
            return False
        # Initialize comparison dictionary
        anagram = dict()
        # Count frequency of characters in string s
        for ch in s:
            if ch in anagram:
                anagram[ch] += 1
                continue
            anagram[ch] = 1

        # Count backward frequency of characters in string t
        for ch in t:
            if ch in anagram:
                anagram[ch] -= 1
                continue
            return False

        for k in anagram:
            if anagram[k]:
                return False
        return True
        