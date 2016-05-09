import time


class Solution(object):
    # first solution
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bfind = False
        for i in xrange(len(nums)):
            if nums[i] >= target:
                continue
            elif bfind is True:
                break
            j = i
            for indices in xrange(len(nums[i+1:])):
                j = j + 1
                if (nums[j] > target):
                    continue
                elif (nums[i]+nums[j]) == target:
                    bfind = True
                    break
        print "index1={}, index2={}".format(i, j+1)
        rel = [i, j+1]
        return rel

    def quickSortMid(self, nums, start, end):
        if (start >= end):
            return
        m_stack = [[start, end], ]
        while (len(m_stack) > 0):
            # print nums,'first:'
            m_current = m_stack.pop()
            low, high = m_current[0], m_current[1]
            midValue = nums[low]
            while low < high:
                while low < high:
                    if nums[high][1] >= midValue[1]:
                        high = high-1
                    else:
                        nums[low] = nums[high]
                        break
                while low < high:
                    if nums[low][1] <= midValue[1]:
                        low = low+1
                    else:
                        nums[high] = nums[low]
                        break
            # print nums,'end:'
            nums[high] = midValue   # low == high
            mid = high
            if (mid-1 > m_current[0]):
                m_stack.append([m_current[0], mid-1])
            if (mid+1 < m_current[1]):
                m_stack.append([mid+1, m_current[1]])
        # self.quickSortMid(nums,start,mid-1)
        # self.quickSortMid(nums,mid+1,end)
        return

    def sortedNewNums(self, nums):  # sorted according tuple in the list
        start = 0
        end = len(nums)
        self.quickSortMid(nums, start, end-1)  # from low to high

    def getRelTarget(self, sortednums, target):
        rel = [0, 0]
        m_len = len(sortednums)
        for i in xrange(m_len):
            for j in xrange(i+1, m_len):
                if ((sortednums[i][1] + sortednums[j][1]) > target):
                    break
                elif ((sortednums[i][1] + sortednums[j][1]) == target):
                    a, b = sortednums[i][0]+1, sortednums[j][0]+1
                    if a > b:
                        rel = [b, a]
                    else:
                        rel = [a, b]
                    return rel
        return rel

    def twoSum(self, nums,  target):
        sortednums = []
        m_len = len(nums)
        for i in xrange(m_len):
            newItems = [i, nums[i]]
            sortednums.append(newItems)

        self.sortedNewNums(sortednums)
        rel = self.getRelTarget(sortednums, target)
        return rel

sol = Solution()
a = time.time()
