class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_window_length = 0
        char_map = {}
        max_freq = 0
        for right, ch in enumerate(s):
            char_map[ch] = char_map.get(ch, 0) + 1
            max_freq = max(max_freq, char_map[ch])

            current_window_length = right - left + 1
            if current_window_length - max_freq > k:
                char_map[s[left]] -= 1
                left += 1
            
            current_window_length = right - left + 1
            max_window_length = max(max_window_length, current_window_length)
        return max_window_length