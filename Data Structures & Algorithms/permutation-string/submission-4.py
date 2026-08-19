class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        if s1_len > len(s2):
            return False
        cmp_count, win_count =  [0] * 26, [0] * 26


        base = ord('a')

        for ch in s1:
            cmp_count[ord(ch) - base] += 1
        
        for i in range(s1_len):
            win_count[ord(s2[i]) - base] += 1
        
        if cmp_count == win_count:
            return True

        for i in range(s1_len, len(s2)):
            win_count[ord(s2[i]) - base] += 1
            win_count[ord(s2[i - s1_len]) - base] -= 1
            if cmp_count == win_count:
                return True

        return False

