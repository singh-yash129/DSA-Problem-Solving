class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                # The second pop is the left operand (a - b)
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                b, a = stack.pop(), stack.pop()
                # Use int(a / b) to truncate toward zero
                stack.append(int(a / b))
            else:
                # Convert the string token to an actual integer
                stack.append(int(i))
                
        return stack[0]