class Solution:
    zero = ord('0')
    def multiply(self, num1: str, num2: str) -> str:
        a = self.extractNum(num1)
        b = self.extractNum(num2)
        return str(a * b)
        
    def extractNum(self, num) -> int:
        a = 0
        for ch in num:
            a = a * 10
            a += ord(ch) - self.zero
        return a