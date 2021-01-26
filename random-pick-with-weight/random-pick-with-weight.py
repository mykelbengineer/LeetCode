class Solution:
​
    def __init__(self, w: List[int]):
        self.cum_sum = []
        
        self.cum_sum = [w[0]]
        
        for i in range(1, len(w)):
            self.cum_sum.append(self.cum_sum[i-1] + w[i])
            
    def pickIndex(self) -> int:
        return self.bisect(random.random() * self.cum_sum[-1], self.cum_sum)
        
    
    def bisect(self, target, nums):
        left = 0
        right = len(nums) -1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if target > nums[mid]:
                left = mid + 1
                
            else:
                right = mid
        
        return left
        
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
