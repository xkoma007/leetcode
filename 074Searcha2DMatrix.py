class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        # find line
        low, high = 0, m-1

        while low < high:
            mid = (low + high) / 2
            if matrix[mid][0] > target:
                high -= 1
            elif matrix[mid][0] < target:
                if matrix[mid][n-1] > target:
                    low = mid
                    break
                elif matrix[mid][n-1] < target:
                    low = mid + 1
                else:
                    return True
            else:
                return True

        if matrix[low][0] > target:
            return False
        target_line = low
        low, high = 0, n-1
        while low < high:
            mid = (low + high) / 2
            if matrix[target_line][mid] < target:
                low = mid + 1
            elif matrix[target_line][mid] > target:
                high = mid - 1
            else:
                return True
        if matrix[target_line][low] == target:
            return True
        else:
            return False

c = Solution()

B = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
print(c.searchMatrix(B, 11))
