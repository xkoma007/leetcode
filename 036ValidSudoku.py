class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        entrys = []
        for pos, cur_entry in enumerate(board):
            entrys.append([])
            for val in cur_entry:
                if val == '.':
                    entrys[pos].append(0)
                elif val in entrys[pos]:
                    return False
                else:
                    entrys[pos].append(val)

        m_len = len(entrys)
        # compare cur col  entry
        compare_nums = []
        for col in range(m_len):
            compare_nums = []
            for pos in range(m_len):
                if entrys[pos][col] == 0:
                    continue
                elif entrys[pos][col] not in compare_nums:
                    compare_nums.append(entrys[pos][col])
                else:
                    return False
        # compare nine square
        x, y = 0, 0
        for _ in range(3):
            for _ in range(3):
                compare_nums = []
                m, n = x, y
                for i in range(3):
                    m = x + i
                    for j in range(3):
                        n = y + j
                        if entrys[m][n] == 0:
                            continue
                        elif entrys[m][n] not in compare_nums:
                            compare_nums.append(entrys[m][n])
                        else:
                            return False
                y += 3
            x += 3
            y = 0
        return True
