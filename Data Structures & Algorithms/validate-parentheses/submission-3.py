class Solution:
    def isValid(self, s: str) -> bool:
        cmp = {')': '(', '}': '{', ']': '['}
        hold = list()

        for ch in s:
            if ch in cmp:
                if not hold or cmp[ch] != hold.pop():
                    return False
            else:
                hold.append(ch)

        return (not hold)