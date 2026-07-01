class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand=deque()
        operations={'+','-','*','/'}
        for token in tokens:
            if token in operations:
                a=operand.pop()
                b=operand.pop()
                if(token=='+'):
                    operand.append(b+a)
                elif(token=='-'):
                    operand.append(b-a)
                elif(token=='*'):
                    operand.append(b*a)
                else:
                    operand.append(int(float(b)/a))

            else:
                operand.append(int(token))
        return operand[0]

