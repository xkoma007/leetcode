class Solution(object):
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """

    #     if len(nums1) == 0:
    #         nums1 = nums2
    #     return nums1
    #     m_low = 0
    #     m_high = len(nums1) - 1
    #     for m_val in nums2:
    #         #  search
    #         while m_low < m_high:
    #             m_mid = (m_low + m_high) // 2
    #             if m_val >= nums1[m_mid]:
    #                 m_low = m_mid + 1
    #             else:
    #                 m_high = m_mid - 1
    #         if m_val < nums1[m_low]:
    #             nums1.insert(m_low, m_val)
    #         elif m_low == len(nums1) - 1:
    #             nums1.append(m_val)
    #         else:
    #             nums1.insert(m_low+1, m_val)
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        m_pos1 = 0
        m_newlen = m
        for i in range(n):
            if m_newlen == 0:
                nums1.insert(0, nums2[i])
            elif nums2[i] <= nums1[m_pos1]:
                nums1.insert(m_pos1, nums2[i])
                m_pos1 += 1
            else:
                while m_pos1 <= (m_newlen - 1) and nums2[i] > nums1[m_pos1]:
                    m_pos1 += 1
                if m_pos1 > (m_newlen - 1):
                    if m_newlen < len(nums1):
                        nums1[m_pos1] = nums2[i]
                    else:
                        nums1.append(nums2[i])
                else:
                    nums1.insert(m_pos1, nums2[i])
                    m_pos1 += 1
            m_newlen += 1
        m_rlen = len(nums1)
        if m_rlen > m_newlen:
            del nums1[m_newlen: m_rlen]
        return 
c = Solution()
print(c.merge([1,0],1,[2],1))
