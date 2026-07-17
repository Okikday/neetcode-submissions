class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map: dict[str, int] = {}

        for letter in s:
            if letter in s_map:
                s_map[letter] = s_map.get(letter) + 1
            else:
                s_map[letter] = 1

        for letter in t:
            if letter in s_map:
                count = s_map.get(letter)
                if count == 1:
                    s_map.pop(letter)
                else:
                    s_map[letter] = count - 1
            else:
                return False

        return len(s_map) == 0

        