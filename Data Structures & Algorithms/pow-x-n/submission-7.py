class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)

        if abs(float(x)) == 1:
            if n & 1 == 0: #if even
                return abs(x)
            if x < 0:
                return -float(1)
            else:
                return float(1)
        if n <= -(2**31) or n >= (2**32):
            return float(0)
        x = x if n > 0 else (1/x)
        res = x
        for i in range(1, (n if n > 0 else -n)):
            res *= x
        return res