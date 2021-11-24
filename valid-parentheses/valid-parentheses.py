class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {'}':'{', ']':'[', ')':'('}
        
        stack = []
        
        for i in s:
            if i in paren_map and stack:
                if stack.pop() != paren_map[i]:
                    return False
                
            else:
                stack.append(i)
                
        return not stack
        