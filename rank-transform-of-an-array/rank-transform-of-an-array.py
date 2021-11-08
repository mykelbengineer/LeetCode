class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(set(arr))
        index_of_array = {}
        output = []
        
        i = 0
        while i < len(sorted_array):
            index_of_array[sorted_array[i]] = i 
            i += 1
            
        
        for i in range(len(arr)):
            output.append(index_of_array[arr[i]] + 1)
            
        return output
            
        
        
        
        
        
        