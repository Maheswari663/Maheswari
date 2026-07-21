class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
       
        if endWord not in wordSet:
            return 0
            
       
        queue = deque([(beginWord, 1)])
        
        
        while queue:
            current_word, level = queue.popleft()
            
           
            if current_word == endWord:
                return level
                
           
            for i in range(len(current_word)):
                original_char = current_word[i]
                
                
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                        
                  
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                   
                    if next_word in wordSet:
                        queue.append((next_word, level + 1))
                        wordSet.remove(next_word) 
        return 0    

                        