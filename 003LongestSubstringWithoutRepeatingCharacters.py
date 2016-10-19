class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dynamic programming
        m_substr = []
        m_sublen = []
        m_len = len(s)
        m_match = False
        m_index = 0
        m_newindex = 0
        m_max = 0

        if m_len == 1:
            return 1
        m_substr.append(m_index)
        while m_index < (m_len - 1):
            m_newindex =  m_index + 1
            while m_newindex < m_len :
                i =  m_index
                while i <  m_newindex:
                    if s[m_newindex] == s[i]:
                        m_match = True
                        break;
                    i =  i + 1
                if m_match:
                    m_substr.append(m_newindex)
                    m_tmplen = m_newindex - m_index 
                    if m_max < m_tmplen:
                        m_max = m_tmplen
                    m_sublen.append(m_tmplen)
                    m_match = False
                    m_index = m_newindex
                    break;
                else:
                    m_newindex += 1
            if m_newindex >= m_len :
                m_tmplen = m_newindex - m_index
                m_sublen.append(m_tmplen)
                if m_max <  m_tmplen:
                    m_max = m_tmplen
                break;

        return m_max

a = Solution()
print a.lengthOfLongestSubstring("dvdf")
print 'hehe'



            
            




                

                
                
                
                
            
                
                
                
            
            
            
            
            
            

            
        
        

        
