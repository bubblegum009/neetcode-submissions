class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)):
            return False
        i=0
        while(i<=len(s2)-len(s1)):
            sub=s2[i:i+len(s1)]
            if(sorted(sub)==sorted(s1)):
                return True
            i+=1
        return False
