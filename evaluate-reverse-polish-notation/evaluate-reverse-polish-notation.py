class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def is_num(s):
            try:
                int(s)
                return True
            
            except:
                return False
            
        
        for token in tokens:
            if is_num(token):
                stack.append(token)
                
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                
                if token == "+":
                    num = second + first
                elif token == "-":
                    num = second - first
                elif token == "*":
                    num = second * first
                elif token == "/":
                    num = int(second / first)
                    
                stack.append(str(num))
            
        
        return stack[-1]
        