# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                if mid == 1:
                    return mid
                elif not isBadVersion(mid-1):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return 0
