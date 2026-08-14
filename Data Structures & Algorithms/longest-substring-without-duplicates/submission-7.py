class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        longest = l = r = 0

        for i in range(len(s)):
            
            if s[i] in found:
                ch = s[i]
                longest = max(longest, r-l)
                while s[l] != ch:
                    found.remove(s[l])
                    l += 1
                l += 1
                r += 1
                continue
            r += 1
            found.add(s[i])

        return max(longest, r-l)