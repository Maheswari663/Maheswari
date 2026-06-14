class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)




        def backtrack(start_idx, current_target, path):
            if current_target == 0:
                res.append(list(path))
                return
            
            for i in range(start_idx, n):
               
                if candidates[i] > current_target:
                    break
                
               
                if i > start_idx and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
              
                backtrack(i + 1, current_target - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return res