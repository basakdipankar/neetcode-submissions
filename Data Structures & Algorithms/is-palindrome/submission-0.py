class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        ord_A = ord('A')
        ord_Z = ord_A + 25
        ord_a = ord('a')
        ord_z = ord_a + 25
        ord_0 = ord('0')
        ord_9 = ord_0 + 9
        while left < right:
            ord_left = ord(s[left])
            if not ((ord_left >= ord_A and ord_left <= ord_Z) or \
                (ord_left >= ord_a and ord_left <= ord_z) or \
                (ord_left >= ord_0 and ord_left <= ord_9)):
                left += 1
                continue
            ord_right = ord(s[right])
            if not ((ord_right >= ord_A and ord_right <= ord_Z) or \
                (ord_right >= ord_a and ord_right <= ord_z) or \
                (ord_right >= ord_0 and ord_right <= ord_9)):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        