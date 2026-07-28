class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} 
        
        def dfs(r, c, prev_val):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev_val:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
                
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
            
        max_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r, c, -1))
                
        return max_path