class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        p_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        if not digits:
            return []
        
        res = ['']
        
        for i in range(len(digits)):
            res = [prev + letter for prev in res for letter in p_map[digits[i]]]
        
        return res
