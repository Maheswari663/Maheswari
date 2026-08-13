class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        charset=set()
        
        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[R])
            res=max(res,R-l+1)

        return res

        
        
