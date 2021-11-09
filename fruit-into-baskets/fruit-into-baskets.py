class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = 2
        output = float(-inf)
        left = 0
        fruit_freq = defaultdict(int)
        
        for right in range(len(fruits)):
            right_fruit = fruits[right]
            fruit_freq[right_fruit] += 1
            
            
            while len(fruit_freq) > baskets:
                left_fruit = fruits[left]
                fruit_freq[left_fruit] -= 1
                if fruit_freq[left_fruit] == 0:
                    del fruit_freq[left_fruit]
                left += 1
                    
            output = max(output, right - left + 1)
            
        
        return output
        