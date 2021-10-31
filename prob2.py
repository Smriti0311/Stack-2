# Time Complexity : 
# Space Complexity :
# Did this code successfully run on Leetcode : 
# Any problem you faced while coding this : 

# Your code here along with comments explaining your approach


from collections import deque

class Solution:
    def isValid(self, s):

        if s is None or len(s) == 0:
            return True
        
        st = deque()
        for i in range(len(s)):

            c = s[i]
            if c == '(':
                st.append(')')
            elif c == '{':
                st.append('}')
            elif c == '[':
                st.append(']')
            elif len(st) == 0 or c != st.pop():
                return False
        
        return len(st) == 0
        