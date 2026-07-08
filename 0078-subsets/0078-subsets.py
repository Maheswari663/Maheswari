class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(index, path):
           
            res.append(list(path))
            
            for i in range(index, n):
               
                path.append(nums[i])
                
                backtrack(i + 1, path)
               
                path.pop()
                
        backtrack(0, [])
        return res