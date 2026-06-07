class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary
        groups = dict()
        # Loop through array of strings
        for st in strs:
            # Sort the string into alphabetical order
            sorted_st = ''.join(sorted(st))
            # Search in dictionary to find such key i.e sorted string
            if sorted_st in groups:
                # If yes, append the original string into the key's value which is a list
                groups[sorted_st].append(st)
                continue
            # Else, add the key and values as a list containing the original string as an element
            groups[sorted_st] = [st]
        return list(groups.values())
