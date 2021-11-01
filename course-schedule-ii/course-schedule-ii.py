class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        todoList = {i:set() for i in range(numCourses)}
        graph = defaultdict(set)
        output = []
        
        for crs, pre in prerequisites:
            todoList[crs].add(pre)
            graph[pre].add(crs)
            
        q = deque([])
        
        for crs, pre in todoList.items():
            if len(pre) == 0:
                q.append(crs)

        
        while q:
            
            pre = q.popleft()

            for crs in graph[pre]:
                todoList[crs].remove(pre)
                if len(todoList[crs]) == 0:
                    q.append(crs)
                    
            todoList.pop(pre)
            output.append(pre)
            
        
        if not todoList: 
            return output 
        else: 
            return []