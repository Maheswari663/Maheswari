class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)
        
       
        def backtrack(idx, current_target, path):
          
            if current_target == 0:
                res.append(list(path))
                return
            
           
            if current_target < 0 or idx == n:
                return
            
            
            path.append(candidates[idx])
          
            backtrack(idx, current_target - candidates[idx], path)
            
            
            path.pop()
            backtrack(idx + 1, current_target, path)

        backtrack(0, target, [])
        return res
  