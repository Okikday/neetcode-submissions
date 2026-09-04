import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distmap = dict()
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            if dist not in distmap:
                distmap[dist] = list()
            distmap[dist].append(point)
        pheap = list(distmap.items())
        heapq.heapify(pheap)
        
        res = list(pheap[0][1])
        if len(res) >= k:
            return res[0:k]
        heapq.heappop(pheap)
        while len(res) < k:
            if len(pheap[0][1]) < k - len(res):
                res = res + pheap[0][1]
                heapq.heappop(pheap)
            else:
                res = res + pheap[0][1][0:k - len(res)]

        return res

