class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = []
        for m_val in nums:
            if not max_list:
                max_list.append(m_val)
            else:
                for m_pos, m_cur in enumerate(max_list):
                    if m_val > m_cur:
                        max_list.insert(m_pos, m_val)
                        if len(max_list) > 3:
                            max_list.pop()
                        break
                    elif m_val == m_cur:
                        break
                    else:
                        if m_pos == (len(max_list) - 1) and len(max_list) < 3:
                            max_list.append(m_val)
                            break
                        else:
                            continue
        return max_list[0] if len(max_list) < 3 else max_list[2]

c = Solution()
print(c.thirdMax([3, 2, 1]))
print(c.thirdMax([1, 2]))
print(c.thirdMax([2, 2, 3, 1]))
