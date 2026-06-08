class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = nums_dict.get(n, False)
        max_lcs = 0
        for n in nums:
            if nums_dict[n]:
                continue
            current_lcs = 1
            nums_dict[n] = True

            next_ele = n + 1
            while next_ele in nums_dict and not nums_dict[next_ele]:
                current_lcs += 1
                nums_dict[next_ele] = True
                next_ele = next_ele + 1

            prev_ele = n - 1
            while prev_ele in nums_dict and not nums_dict[prev_ele]:
                current_lcs += 1
                nums_dict[next_ele] = True
                prev_ele = prev_ele - 1

            max_lcs = max(max_lcs, current_lcs)
        return max_lcs

            