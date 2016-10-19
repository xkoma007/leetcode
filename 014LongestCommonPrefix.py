class Solution(object):
    def judge_common_prefixstr(self, str, prefixstr):

        match_prefix = True
        for index, ch in enumerate(prefixstr):
            if ch != str[index]:
                match_prefix = False
        return match_prefix

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        min_strlen = len(strs[0])
        min_index = 0

        for index, sub_str in enumerate(strs):
            if len(sub_str) < min_strlen:
                min_strlen = len(sub_str)
                min_index = index

        min_str = strs[min_index]

        if min_str == []:
            return ""

        max_pos = len(min_str)
        longest_str = ""

        for __ in xrange(len(min_str)):
            current_str = min_str[0:max_pos]
            success = True
            for i, sub_str in enumerate(strs):
                success = self.judge_common_prefixstr(sub_str, current_str)
                if not success:
                    max_pos -= 1
                    break
            if success:
                longest_str = current_str
                break

        return longest_str

a = Solution()
print a.longestCommonPrefix([])
