class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        longest = 0

        l = r = 0

        for i in range(len(s)):
            ch = s[i]
            if ch in found:
                #print(f"exists: {ch}, l: {l}, r: {r}, longest: {r-l}")
                longest = max(longest, r-l)
                while s[l] != ch:
                    found.remove(s[l])
                    l += 1
                    
                l += 1
                #print(f"newL: {l}, r: {r}")
                found.remove(ch)
            r += 1
            found.add(ch)

        return max(longest, r-l)