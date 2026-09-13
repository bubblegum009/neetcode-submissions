class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sublen=0
        lastseen={}
        start=0
        for  i in range(0,len(s)):
            ch=s[i]
            if ch in lastseen and lastseen[ch]>=start:
                start=lastseen[ch]+1
            
            sublen=max(sublen,i-start+1)
            lastseen[ch]=i

        return sublen