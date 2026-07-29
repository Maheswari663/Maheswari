class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            
      
        visitSet = set()

        def dfs(crs):
            if crs in visitSet: 
                return False
            if adj[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            adj[crs] = [] 
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True