class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        new_num = n
        nums = [new_num]
        happy_rel = True

        while new_num != 1:
            cur_val = new_num
            new_num = 0
            while cur_val != 0:
                new_num += (cur_val % 10) ** 2
                cur_val = cur_val // 10
            if new_num not in nums:
                nums.append(new_num)
            else:
                happy_rel = False
                break
        return happy_rel
