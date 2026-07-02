class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            # As long as I am finding any opening bracket, I will push it to a stack
            if ch in ('(', '{', '['):
                stack.append(ch)
            # I find any closing bracket, I will pop from stack and compare
            if ch in (')', '}', ']'):
                if not stack:
                    return False
                top_el = stack.pop()
                if (top_el == '(' and ch == ')') or (top_el == '{' and ch == '}') or (top_el == '[' and ch == ']'):
                    continue
                return False
            # print(stack)

        if not stack:
            return True
        return False