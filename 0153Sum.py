class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m_sets = []
        m_list = []
        m_len = len(nums)
        for index, val in enumerate(nums):
            if (index + 2) == m_len:
                break
            left_sum = 0 - val
            m_list = []
            m_list.append(val)
            newnums = nums[index+1:]
            for i, sub_val in enumerate(newnums):
                # print index,i
                if (i + 1) == len(newnums):
                    break
                left_sum -= sub_val
                m_list.append(sub_val)
                if left_sum in newnums[i+1:]:
                    m_list.append(left_sum)
                    import copy
                    new_list = copy.deepcopy(m_list)
                    new_list.sort()
                    if new_list in m_sets:
                        pass
                    else:
                        m_sets.append(new_list)
                    # restore data
                    left_sum = 0 - val
                    m_list.pop()
                    m_list.pop()
                else:
                    left_sum = 0 - val
                    m_list.pop()

        return m_sets

a = Solution()
print a.threeSum([-7,-10,-1,3,0,-7,-9,-1,10,8,-6,4,14,-8,9,-15,0,-4,-5,9,11,3,-5,-8,2,-6,-14,7,-14,10,5,-6,7,11,4,-7,11,11,7,7,-4,-14,-12,-13,-14,4,-13,1,-15,-2,-12,11,-14,-2,10,3,-1,11,-5,1,-2,7,2,-10,-5,-8,-10,14,10,13,-2,-9,6,-7,-7,7,12,-5,-14,4,0,-11,-8,2,-6,-13,12,0,5,-15,8,-12,-1,-4,-15,2,-5,-9,-7,12,11,6,10,-6,14,-12,9,3,-10,10,-8,-2,6,-9,7,7,-7,4,-8,5,-4,8,0,3,11,0,-10,-9])
