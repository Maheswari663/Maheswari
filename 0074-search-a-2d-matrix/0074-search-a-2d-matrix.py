class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        low = 0
        high = (rows * cols) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
           
            r = mid // cols
            c = mid % cols
            
            mid_val = matrix[r][c]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False