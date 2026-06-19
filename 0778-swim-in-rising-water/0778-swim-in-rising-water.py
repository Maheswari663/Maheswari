class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, r, c)
        
        while min_heap:
            elevation, r, c = heapq.heappop(min_heap)
            
            if r == n - 1 and c == n - 1:
                return elevation
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    next_elevation = max(elevation, grid[nr][nc])
                    heapq.heappush(min_heap, (next_elevation, nr, nc))
                    
        return 0