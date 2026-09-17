class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        chs1=[0]*26
        chs2=[0]*26

        for i in range(0,len(s1)):
            chs1[ord(s1[i])-ord('a')]+=1
            chs2[ord(s2[i])-ord('a')]+=1

        if chs1==chs2:
            return True
        
        for j in range(len(s1),len(s2)):
            #Add new character to the ch2 array
            chs2[ord(s2[j])-ord('a')]+=1

            #Remove start of the window
            rch=j-len(s1)
            chs2[ord(s2[rch])-ord('a')]-=1

            if chs1==chs2:
                return True
        return False