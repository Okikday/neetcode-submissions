class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        available = set(s)
        longest = 0

        for ch in available:
            l = count = 0
            for r in range(len(s)):
                if s[r] == ch:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == ch:
                        count -= 1
                    l += 1
                longest = max(longest, r-l+1)
        return longest
            
