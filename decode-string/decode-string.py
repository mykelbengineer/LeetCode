class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ''
        k = 0
        
        for i in s:
            if i == '[':
                stack.append((curr_string, k))
                curr_string, k = '', 0
                
            elif i == ']':
                last_string, last_k = stack.pop()
                curr_string = last_string + last_k * curr_string
                
            elif i.isdigit():
                k = k * 10 + int(i)
            
            else:
                curr_string += i
                
        
        return curr_string