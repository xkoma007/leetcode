class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, total_gas, tank = 0, 0, 0
        for i, (cur_gas, cur_cost) in enumerate(zip(gas, cost)):
            tank += cur_gas - cur_cost
            total_gas += cur_gas - cur_cost
            if tank < 0:
                tank = 0
                start = i+1
        return start if total_gas >= 0 else -1
c = Solution()
print(c.canCompleteCircuit([1,2,3,3], [2,1,5,1]))
