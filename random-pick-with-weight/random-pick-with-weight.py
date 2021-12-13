import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        self.total = 0
        
        total_weight_so_far = 0
        for weight in w:
            total_weight_so_far = weight + total_weight_so_far
            self.prefix_sums.append(total_weight_so_far)
            
        self.total = total_weight_so_far
        

    def pickIndex(self) -> int:
        random_num = random.random()  * self.total
        
        left = 0
        right = len(self.prefix_sums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            midVal = self.prefix_sums[mid]
            
            if midVal > random_num:
                
                right = mid
                
            else:
                
                left = mid + 1
                
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()