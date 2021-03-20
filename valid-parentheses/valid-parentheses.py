class Solution:
    def isValid(self, s: str) -> bool:
        paren_set = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for brace in s:
            if brace in paren_set:
                top_elem = stack.pop() if stack else '#'
                
                if paren_set[brace] != top_elem:
                    return False
            else:
                
                stack.append(brace)
                
        return not stack