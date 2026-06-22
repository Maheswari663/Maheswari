class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(path, used):
           
            if len(path) == n:
                res.append(list(path)) 
                return
            
            for i in range(n):
               
                if nums[i] in used:
                    continue
                
              
                path.append(nums[i])
                used.add(nums[i])
                
               
                backtrack(path, used)
                
              
                path.pop()
                used.remove(nums[i])
        
        backtrack([], set())
        return res 