class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char: i for i, char in enumerate(s)}
        
        result = []
        size = 0
        end = 0
        
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_index[char])
            
            if i == end:
                result.append(size)
                size = 0
                
        return result