class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dic = defaultdict(lambda:[])

        for word in words:
            dic[word[0]].append(deque(word))

        ans = 0
        for letter in s:
            
            temp = dic[letter]
            dic[letter] = []
            
            for word in temp:
                
                word.popleft() 
                if word:
                    dic[word[0]].append(word)
                else:
                    ans += 1
                    
        return ans
                    
                    
                
        
        
        

        