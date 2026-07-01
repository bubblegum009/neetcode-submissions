class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        brackets={
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in range(0,len(s)):
            ch=s[i]
            if ch in brackets.keys():
                st.append(ch)
            elif ch in brackets.values():
                if(len(st)==0):
                    return False
                t=st.pop()
                if(brackets[t]!=ch):
                    return False

        return len(st)==0
                    
