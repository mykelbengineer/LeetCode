class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.backtrack(output, "", 0, 0, n)
        
        return output
        
        
    
    
    def backtrack(self, output_list, curr_string, num_open, num_close, max_paren):
        
        if len(curr_string) == max_paren * 2:
            output_list.append(curr_string)
            return
        
        if num_open < max_paren:
            self.backtrack(output_list, curr_string + "(", num_open + 1, num_close, max_paren)
            
        if num_close < num_open:
            self.backtrack(output_list, curr_string + ")", num_open, num_close + 1, max_paren)
        