class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def is_palindrome(sub):
          
            return sub == sub[::-1]

        def backtrack(start, path):
          
            if start == n:
                res.append(list(path))
                return
            
           
            for i in range(start, n):
                substring = s[start : i + 1]
                
             
                if is_palindrome(substring):
                   
                    path.append(substring)
                 
                    backtrack(i + 1, path)
                  
                    path.pop()

        backtrack(0, [])
        return res