class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        map_s, map_g = dict(), dict()
        n_bulls, n_cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                n_bulls += 1
            else:
                if s not in map_s:
                    map_s[s] = 1
                else:
                    map_s[s] += 1
                if g not in map_g:
                    map_g[g] = 1
                else:
                    map_g[g] += 1

        for key in map_g:
            if key in map_s:
                if map_g[key] >= map_s[key]:
                    n_cows += map_s[key]
                else:
                    n_cows += map_g[key]
        return str(n_bulls) + "A" + str(n_cows) + "B"

c = Solution()
print(c.getHint("1807", "7810"))
print(c.getHint("1123", "0111"))
