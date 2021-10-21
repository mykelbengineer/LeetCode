class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        
        B = sorted([(v,i) for i,v in enumerate(nums2)])
        
        N = len(nums1)
        
        output = [-1] * N
        
        left,right = 0, N-1
        
        for i in range(N-1,-1,-1):
            if nums1[right] > B[i][0]:
                output[B[i][1]] = nums1[right]
                right -= 1
                
            else:
                output[B[i][1]] = nums1[left]
                left += 1
                
        return output
                
        