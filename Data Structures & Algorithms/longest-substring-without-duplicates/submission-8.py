class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        longest = l = 0

        for r in range(len(s)):
            if s[r] in found:
                while s[l] != s[r]:
                    found.remove(s[l])
                    l += 1
                l += 1
            found.add(s[r])
            longest = max(longest, r-l+1)

        return longest