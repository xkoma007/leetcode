class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map_s = dict()
        for ch in s:
            if ch not in map_s:
                map_s[ch] = 1
            else:
                map_s[ch] += 1

        for ch in t:
            if ch not in map_s:
                return ch
            else:
                map_s[ch] -= 1
                if map_s[ch] < 0:
                    return ch
                
