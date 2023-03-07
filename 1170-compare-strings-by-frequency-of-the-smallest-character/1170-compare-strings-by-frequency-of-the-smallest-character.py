class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        
        def f(string):
            
            count = Counter(string)
            sortd = sorted(count.items(), key = lambda x: x[0])
            
            return sortd[0][1]
        
        
        
        for i in range(len(words)):
            words[i] = f(words[i])
            
        words.sort()
        
        
        def findWords(num):
            
            left = -1
            right = len(words) - 1
            
            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if words[mid] > num:
                    right = mid
                    
                else:
                    left = mid
            
            return len(words) - right  if words[right] > num else 0
        
        
        for i in range(len(queries)):
            temp = f(queries[i])
            numOfGreater= findWords(temp)
            
            queries[i] = numOfGreater
            
        return queries
        
        
        