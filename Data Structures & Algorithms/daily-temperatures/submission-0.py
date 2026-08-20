class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = list()
        lo, hi = 0, 0
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]
            if temp >= hi:
                hi = temp
                res.append(0)
            else:
                for x in range(i+1, len(temperatures)):
                    if temperatures[x] > temp:
                        res.append(x - i)
                        break
            
        res.reverse()
        return res