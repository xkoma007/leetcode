class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_s = dict()
        for ch in s:
            if ch not in map_s:
                map_s[ch] = 1
            else:
                map_s[ch] += 1
        num_one = 0
        num_even = 0

        for pos in map_s:
            num_one += map_s[pos] % 2
            num_even += (map_s[pos] // 2) * 2
        if num_one:
            num_one = 1
        return num_one + num_even

c = Solution()
print(c.longestPalindrome("abccccdd"))
