class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digits_sum(n: int) -> int:
            total = 0

            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            return total

        seen: set[int] = set()

        curr = n
        while curr not in seen:
            if curr == 1:
                return True
            seen.add(curr)
            curr = square_digits_sum(curr)

        return False

    
