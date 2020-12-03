class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_pointer = len(S) - 1
        t_pointer = len(T) - 1
        
        s_skips = t_skips = 0
        
        while s_pointer >= 0 or t_pointer >= 0:
            
            while s_pointer >= 0:
                if S[s_pointer] == '#':
                    s_skips += 1
                    s_pointer -= 1
                elif s_skips > 0:
                    s_pointer -= 1
                    s_skips -= 1
                else:
                    break
                    
            while t_pointer >= 0:
                if T[t_pointer] == '#':
                    t_skips += 1
                    t_pointer -= 1
                elif t_skips > 0:
                    t_pointer -= 1
                    t_skips -= 1
                else:
                    break
                    
            if s_pointer >= 0 and t_pointer >= 0 and S[s_pointer] != T[t_pointer]:
                return False
            
            if (s_pointer >= 0) != (t_pointer >= 0):
                return False
            
            s_pointer -= 1
            t_pointer -= 1
            
        
        
        return True
