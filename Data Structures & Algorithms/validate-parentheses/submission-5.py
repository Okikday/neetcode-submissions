class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')': '(', '}': '{', ']': '['}
        stack = list()

        for ch in s:
            if ch in paren:
                if not stack or paren[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)

        return not stack