import copy


class Solution(object):
    def restore_ip(self, left_num, s, cur_rel, total_rels):
        if not left_num and not len(s):
            total_rels.append('.'.join(cur_rel))
            return
        if not len(s):
            return
        new_rel = copy.copy(cur_rel)
        new_rel.append(s[0])
        self.restore_ip(left_num-1, s[1:], new_rel, total_rels)
        if len(s) >= 2 and s[0] != '0':
            new_rel = copy.copy(cur_rel)
            new_rel.append(s[0:2])
            self.restore_ip(left_num-1, s[2:], new_rel, total_rels)
        if len(s) >= 3 and int(s[0:3]) <= 255 and s[0] != '0':
            new_rel = copy.copy(cur_rel)
            new_rel.append(s[0:3])
            self.restore_ip(left_num-1, s[3:], new_rel, total_rels)
        return

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        total_rels = []
        if len(s) > 12:
            return total_rels
        self.restore_ip(4, s, [], total_rels)
        return total_rels

c = Solution()
print(c.restoreIpAddresses("25525511135"))
