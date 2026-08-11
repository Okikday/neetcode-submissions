class Solution:
    def isPalindrome(self, s: str) -> bool:
        it = "".join(c.lower() for c in s if c.isalnum() and c.isascii())
        return it[::-1] == it