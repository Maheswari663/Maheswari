class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(base, exp):
            if exp == 0:
                return 1
            
           
            half = solve(base, exp // 2)
            
          
            if exp % 2 == 0:
                return half * half
           
            else:
                return base * half * half

       
        if n < 0:
            return 1 / solve(x, abs(n))
        
        return solve(x, n)