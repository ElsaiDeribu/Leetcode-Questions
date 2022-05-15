class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dictionary = Counter(s)
        
        ans = ''
        for i in order:
            ans +=  (i * dictionary[i])
            del dictionary[i]
                
        for i in dictionary:
            ans += i * dictionary[i]
                
        return ans
            
            
        