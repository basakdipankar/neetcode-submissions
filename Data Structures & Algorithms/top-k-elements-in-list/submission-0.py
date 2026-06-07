class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Maintain a dictionary counter
        freq_count = {}
        for n in nums:
            freq_count[n] = freq_count.get(n, 0) + 1
        
        # Sort the dictionary based on the values in dictionary
        result = []
        sorted_freq = sorted(freq_count, key=lambda x: freq_count[x])
        for i in range(k):
            result.append(sorted_freq[-1-i])
        return result