class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen={}
        start=0
        substringlen=0
        for i in range(0,len(s)):
            if(s[i] in last_seen and last_seen[s[i]]>=start):
                start= last_seen[s[i]]+1
            last_seen[s[i]]=i
            substringlen=max(substringlen,i-start+1)


        return substringlen
