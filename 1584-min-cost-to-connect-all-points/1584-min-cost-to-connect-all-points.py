class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
       
        visit = set()
        
        
        min_heap = [[0, 0]]
        
        total_cost = 0
        
        
        while len(visit) < N:
            cost, i = heapq.heappop(min_heap)
            
           
            if i in visit:
                continue
                
           
            visit.add(i)
            total_cost += cost
            
           
            for next_i in range(N):
                if next_i not in visit:
                    
                    dist = abs(points[i][0] - points[next_i][0]) + abs(points[i][1] - points[next_i][1])
                    heapq.heappush(min_heap, [dist, next_i])
                    
        return total_cost