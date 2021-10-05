# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = 0
        R = n - 1
        
        while L <= R:
            mid_val = (L + R) // 2
            
            if isBadVersion(mid_val):
                R = mid_val - 1
                
            else:
                L = mid_val + 1
                
        
        return L
            
            
            