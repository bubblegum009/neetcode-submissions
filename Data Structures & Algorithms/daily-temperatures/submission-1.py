class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        i=0
        while(i<len(temperatures)-1):
            j=i+1
            while(j<=len(temperatures)-1):
                if(temperatures[j]>temperatures[i]):
                    result[i]=(j-i)
                    break
                j+=1
            i+=1
        return result
       
    
