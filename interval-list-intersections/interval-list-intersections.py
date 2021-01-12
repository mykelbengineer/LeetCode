class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        Output = []
        m = len(firstList)
        n = len(secondList)
        
        i = j = 0
        
        while i < m and j < n:
            if secondList[j][0] <= firstList[i][-1] and firstList[i][0] <= secondList[j][-1]:
                Output.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][-1], secondList[j][-1])])
                
            if firstList[i][-1] < secondList[j][-1]:
                i += 1
            
            else:
                
                j += 1
                
        
        return Output
