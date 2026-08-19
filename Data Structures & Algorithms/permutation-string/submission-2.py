class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1: dict[int] = dict()
        for i in range(len(s1)):
            map1[s1[i]] = map1.get(s1[i], 0) + 1

        s1_len = len(s1)
        
        
        l = 0
        
        for r in range(len(s2)):
            if s2[r] not in map1:
                while l < r and s2[l] not in map1:
                    l += 1

            while (r - l) == s1_len:
                left = l
                map2: dict[int] = dict()

                while s2[left] in map1 and left < r:
                    map2[s2[left]] = map2.get(s2[left], 0) + 1
                    left += 1

                if map1 == map2:
                    return True
                    
                l += 1
                map2[s2[l]] = map2.get(s2[l], 0) - 1
        
        rem = s2[l::]
        if len(rem) == s1_len:
            map3: dict[int] = dict()
            for i in range(l, r+1):
                map3[s2[i]] = map3.get(s2[i], 0) + 1
            if map1 == map3:
                return True

        return False


            