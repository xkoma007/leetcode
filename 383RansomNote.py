class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map_mag = dict()
        for ch in magazine:
            if ch not in map_mag:
                map_mag[ch] = 1
            else:
                map_mag[ch] += 1
        for ch in ransomNote:
            if ch not in map_mag:
                return False
            elif map_mag[ch] == 0:
                return False
            else:
                map_mag[ch] -= 1
        return True

c = Solution()
print(c.canConstruct("aa", "aab"))
