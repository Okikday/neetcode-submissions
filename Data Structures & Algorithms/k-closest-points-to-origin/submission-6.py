import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distmap = dict()
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            distmap.setdefault(dist, [])
            distmap[dist].append(point)
        pheap = list(distmap.items())
        heapq.heapify(pheap)
        
        res = list(pheap[0][1])
        if len(res) < k:
            heapq.heappop(pheap)
            while len(res) < k:
                res = res + pheap[0][1]
                heapq.heappop(pheap)

        return res[0:k]

