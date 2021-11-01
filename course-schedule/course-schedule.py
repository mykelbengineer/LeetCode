from collections import deque
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = {i:set() for i in range(numCourses)}
        graph = defaultdict(set)

        for crs, pre in prerequisites:
            todo[crs].add(pre)
            graph[pre].add(crs)
            
        q = deque([])
        
        for crs,pre in todo.items():
            if len(pre) == 0:
                q.append(crs)
                
        while q:
            pre = q.popleft()
            
            for crs in graph[pre]:
                todo[crs].remove(pre)
                if len(todo[crs]) == 0:
                    q.append(crs)
                    
            
            todo.pop(pre)
                        
        return not todo