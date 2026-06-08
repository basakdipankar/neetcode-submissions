class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded += str(len(st)) + "#" + st
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += str(s[i])
                i += 1
            length = int(num)
            result.append(s[i+1:i+1+length])
            i = i+1+length
        return result

