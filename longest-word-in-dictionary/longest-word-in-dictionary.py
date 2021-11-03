class Solution:
    def longestWord(self, words: List[str]) -> str:
        mem = set(words)
        ans = ""
        
        for i in words:
            length = len(i)
            
            while length > 0 and i[0:length] in mem:
                length -= 1
                
            
            if length == 0 and len(i) >= len(ans):
                
                if len(ans) == len(i):
                    ans = i if i < ans else ans
                    
                else:
                    
                    ans = i
                    
        return ans
        