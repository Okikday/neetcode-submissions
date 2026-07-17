class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#' # in case stack is empty
                if bracket_map.get(char, "€") != top:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0
            

