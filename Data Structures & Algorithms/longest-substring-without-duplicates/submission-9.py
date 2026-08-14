class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = l = 0
        found = set()
        
        for r in range(len(s)):
            while s[r] in found:
                found.remove(s[l])
                l += 1
            found.add(s[r])
            longest = max(longest, len(found))
        return longest