class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()

        curr = n
        while True:
            value = self.square_digits_sum(curr)
            if value == 1:
                return True
            if value in seen:
                return False
            seen.add(value)
            curr = value
        return False

    
    def square_digits_sum(self, n: int) -> int:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total