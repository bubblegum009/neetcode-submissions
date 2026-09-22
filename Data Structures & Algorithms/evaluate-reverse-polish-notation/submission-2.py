class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands=[]
        operations={'+','-','*','/'}

        for token in tokens:
            if token not in operations:
                operands.append(int(token))
                
            else:
                a=operands.pop()
                b=operands.pop()
                if token =="+":
                    operands.append(a+b)
                elif token =="-":
                    operands.append(b-a)
                elif token == "/":
                     operands.append(int(b/a))
                else:
                    operands.append(a*b)

        return operands[0]