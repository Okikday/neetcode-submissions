class Solution:
    def isValid(self, s: str) -> bool:
        cmp = {')': '(', '}': '{', ']': '['}
        hold = list()

        for ch in s:
            if ch in '({[':
                hold.append(ch)

            elif ch in cmp:
                if not hold or cmp[ch] != hold.pop():
                    return False

        return (not hold)