class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        pairs={
            "(":")",
            "{" :"}",
            "[":"]"        }
        for ch in s:
            if ch in pairs.keys():
                stack.append(ch)
            
            elif ch in pairs.values():
                if len(stack)==0:
                    return False
                elif pairs[stack.pop()]!=ch:
                    return False

        return len(stack)==0