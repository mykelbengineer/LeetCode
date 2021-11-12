class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
    
    def find(self, idx):
        if self.root[idx] == idx:
            return idx
        
        self.root[idx] = self.find(self.root[idx])
        return self.root[idx]
    
    def union(self, idx, idy):
        rootX = self.find(idx)
        rootY = self.find(idy)
        
        if rootX != rootY:
            
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1    
                
            self.count -= 1
            
    def getCount(self):
        return self.count
    
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UnionFinda = UnionFind(n)
        
        for e1, e2 in edges:
            UnionFinda.union(e1,e2)
            
        return UnionFinda.getCount()