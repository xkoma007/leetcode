class Solution(object):
    def largestNumber(self, num):
        comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
        num=map(str,num)
        num.sort(cmp=comp,reverse=True)
        if num[0] == "0":
            return "0"
        return "".join(num)
        # return str(int("".join(num)))

c = Solution()
# print(c.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
print(c.largestNumber([121, 12 ]))
