class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_map={}
        for i in range(0,len(s)):
            s_map[s[i]]=s_map.get(s[i],0)+1

        for j in range(0,len(t)):
            ch=t[j]
            s_map[ch]=s_map.get(ch,0)-1
            if s_map[ch] < 0 :
                return False
        return True