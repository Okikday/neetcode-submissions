class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = list()
        lo = hi = 0
        temp_len = len(temperatures)
        for i in range(temp_len-1, -1, -1):
            if temperatures[i] >= hi:
                hi = temperatures[i]
                res.append(0)
            else:
                for x in range(i+1, temp_len):
                    if temperatures[x] > temperatures[i]:
                        res.append(x - i)
                        break
            
        res.reverse()
        return res