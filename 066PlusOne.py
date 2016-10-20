class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        startPos = len(digits) - 1
        add_value = 1

        while startPos >= 0:
            if digits[startPos] + add_value >= 10:
                digits[startPos] = digits[startPos] + add_value - 10
                add_value = 1
                startPos -= 1
            else:
                digits[startPos] += add_value
                add_value = 0
                break

        if add_value == 1:
            new_list = digits
            new_list.insert(0, add_value)
        else:
            new_list = digits

        return new_list

a = Solution()
print a.plusOne([9])
