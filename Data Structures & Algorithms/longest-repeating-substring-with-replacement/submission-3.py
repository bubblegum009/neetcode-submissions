class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Set to store unique characters of s
        charset=set(s)
        sublen=0
        
        #Iterate through each character
        for c in charset:
            l=0
            count=0
            for r in range(len(s)):
                if(s[r]==c):
                    count+=1
                while(r-l+1-count>k):
                    if(s[l]==c):
                        count-=1
                    l+=1
                sublen=max(sublen,r-l+1)

        return sublen