class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rels = []
        if n < 1:
            return rels
        for val in range(1, n+1):
            m = val % 3
            n = val % 5
            cur_str = ''
            if not m:
                cur_str += 'Fizz'
            if not n:
                cur_str += 'Buzz'
            if len(cur_str):
                rels.append(cur_str)
            else:
                rels.append(str(val))
        return rels
c = Solution()
print(c.fizzBuzz(15))
