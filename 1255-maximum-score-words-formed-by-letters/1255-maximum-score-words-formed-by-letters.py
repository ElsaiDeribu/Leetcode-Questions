class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        
        letters = Counter(letters)
        scr = defaultdict(int)
        
        for i in range(len(score)):
            scr[chr(ord("a") + i)] = score[i]
           
        @lru_cache(None)
        def dp(idx, path):
            
            if idx >= len(words):
                return 0
            
            wd = Counter(words[idx])
            total = 0
            select = 0

            for ltr in wd:
                if wd[ltr] > letters[ltr]:
                    break
            
            else:
                
                for ltr in wd:
                    letters[ltr] -= wd[ltr]
                    total += (scr[ltr] * wd[ltr])
                  
                pathSelect = [i for i in path]
                pathSelect.append(idx)
                pathSelect = tuple(pathSelect)
                
                select = dp(idx + 1, pathSelect) + total
                
                for ltr in wd:
                    letters[ltr] += wd[ltr]
                    
            notSelect = dp(idx + 1, path)
            
            return max(select, notSelect)
                    
                 
        return dp(0,())
            
        
            