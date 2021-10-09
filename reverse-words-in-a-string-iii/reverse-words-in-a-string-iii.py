class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()
        smp = []
        
        for i in tmp:
            i = i[::-1]
            smp.append(i)
            
        return ' '.join(smp)
        