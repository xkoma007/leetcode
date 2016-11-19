from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for ana in strs:
            groups["".join(sorted(ana))].append(ana)
        return groups.values()
c = Solution()
print(c.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
