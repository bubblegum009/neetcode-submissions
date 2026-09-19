class Solution:
    def isHappy(self, n: int) -> bool:
        sumdigits=0

        seen=set()

        while(n!=1):
            if n in seen:
                return False
            seen.add(n)

            sumdigits=0
            while(n>0):
                r=n%10
                sumdigits+=r*r
                n=n//10
            n=sumdigits

            
        return True