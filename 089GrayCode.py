class Solution:
    # @return a list of integers
    '''
/*
        The purpose of this function is to convert an unsigned
        binary number to reflected binary Gray code.
 
        The operator >> is shift right. The operator ^ is exclusive or.
*/
unsigned int binaryToGray(unsigned int num)
{
        return (num >> 1) ^ num;
}
 /*
        The purpose of this function is to convert a reflected binary
        Gray code number to a binary number.
*/
unsigned int grayToBinary(unsigned int num)
{
    unsigned int mask;
    for (mask = num >> 1; mask != 0; mask = mask >> 1)
    {
        num = num ^ mask;
    }
    return num;
}

    '''
    def grayCode(self, n):
        if n == 0:
            return [0]
        res = []
        for i in range(pow(2, n)):
            res.append((i >> 1) ^ i)
        return res

c = Solution()
print(c.grayCode(2))
