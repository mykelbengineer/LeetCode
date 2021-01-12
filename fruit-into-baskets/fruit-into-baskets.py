class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket_a = basket_b = -1
        c_basket_b = curr_max = max_count = 0
        
        for fruit in tree:
            if fruit == basket_a or fruit == basket_b:
                curr_max += 1
                
            else:
                curr_max = c_basket_b + 1
                
            
            if fruit == basket_b:
                c_basket_b += 1
            
            else:
                c_basket_b = 1
                
            if fruit != basket_b:
                basket_a = basket_b
                basket_b = fruit
            
            max_count = max(max_count, curr_max)
​
                
        return max_count
        
        
