class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
            
                stack.append(char)
            else:
               
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                # 2. Pop the opening bracket '['
                stack.pop()
                
                # 3. Extract the multiplier 'k' (could be multiple digits like '10')
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                # 4. Multiply the substring by k and push it back onto the stack
                stack.append(int(k) * substr)
                
        # Join the remaining elements in the stack to form the final decoded string
        return "".join(stack)