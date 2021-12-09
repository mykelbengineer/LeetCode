class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return None
        
        merged = self.merge(nums1, nums2)
        if len(merged) % 2 != 0:
            return merged[len(merged)//2]
        
        else:
            mid1 = len(merged)//2
            mid2 = mid1 - 1
            
            return (merged[mid1] + merged[mid2]) / 2
        
        
        
    def merge(self, list1, list2):
        i = 0
        j = 0
        output = []
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                output.append(list1[i])
                i += 1
                
            else:
                output.append(list2[j])
                j += 1
                
        if i < len(list1):
            for ind in range(i, len(list1)):
                output.append(list1[ind])
                
        if j < len(list2):
            for ind in range(j, len(list2)):
                output.append(list2[ind])
                
        return output