class Solution:
    def decodeString(self, s: str) -> str:
        currentString = ""
        k = 0
        stack = []
        
        for char in s:
            
            if char == '[' :
                stack.append((currentString, k))
                currentString = ""
                k = 0
            
            elif char == ']' :
                last_string, last_k = stack.pop(-1)
                currentString = last_string + last_k * currentString
                
            elif char.isdigit() :
                k = k * 10 + int(char)
                
            else:
                currentString += char
                
        
        return currentString
        
