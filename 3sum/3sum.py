class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)
        
        N, P = set(n), set(p)
        
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
                    
        if len(z) >= 3:
            res.add((0,0,0))

        N_S = set(nums)
        
        for s in [n, p]:
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    target = -(s[i] + s[j])
                    if target in N_S:
                        res.add(tuple(sorted([s[i], s[j], target])))
                
        
        return res
        