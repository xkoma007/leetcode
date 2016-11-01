class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        new_str = str.split()
        if len(new_str) != len(pattern):
            return False

        map_str = dict()
        map_str_ops = dict()
        for cur_rel in zip(pattern, new_str):
            if cur_rel[0] not in map_str:
                if cur_rel[1] not in map_str_ops:
                    map_str[cur_rel[0]] = cur_rel[1]
                    map_str_ops[cur_rel[1]] = cur_rel[0]
                else:
                    return False
            elif map_str[cur_rel[0]] == cur_rel[1]:
                continue
            else:
                return False
        return True

c = Solution()
print(c.wordPattern("abba", "dog dog dog dog"))
