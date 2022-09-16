

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for x in tokens:
            if x == '+':
                stack.append(stack.pop() + stack.pop())
                
            elif x == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                
            elif x == '*':
                stack.append(stack.pop() * stack.pop())
                
            elif x == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
                
            else:
                stack.append(int(x))
                
        return stack[0]