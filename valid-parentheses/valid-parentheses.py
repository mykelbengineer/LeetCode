class Solution:
    def isValid(self, s: str) -> bool:
        pa_map = {']':'[', '}':'{', ')':'('}
        stack = []
        
        for brace in s:
            if brace in pa_map:
                last_elem = stack.pop() if stack else '#'
                
                if pa_map[brace] != last_elem:
                    return False
            
            else:
                stack.append(brace)
                
        return not stack
        