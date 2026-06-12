class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Can we consider substring as a window? Yes
        # A substring is nothing but a window whose 
        # maximum length can be the length of the string
        # A valid output is a substring/window in string s 
        # where there is same distinct characters and their frequency as in string t

        # let us first track the charcaters to match and their repective frequency
        if t == "":
            return ""

        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        matched = 0
        needs = len(t_freq)

        # For a valid window it should be matched == needs

        # We will try to iterate over the string characters s
        # Try to main two pointers left, right to find the valid window / substring
        left = 0
        window_freq = {}
        res = [-1, -1]
        resLen = float('infinity')
        for right in range(len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            if s[right] in t_freq and window_freq[s[right]] == t_freq[s[right]]:
                matched += 1

            while matched == needs:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    matched -= 1
                left += 1
        left, right = res

        return s[left: right + 1] if resLen != float('infinity') else ''
