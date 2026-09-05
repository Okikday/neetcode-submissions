class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            bits = bin(i).replace("0b", "")
            count = 0
            for b in bits:
                if b == '1':
                    count += 1
            res.append(count)

        return res
                


