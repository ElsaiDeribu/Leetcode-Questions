class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dictionary = Counter(s)
        ans =[]
        
        for i in order:
            while dictionary[i] != 0:
                ans.append(i)
                dictionary[i] -= 1
                
            if dictionary[i] == 0:
                del dictionary[i]
                
        for i in dictionary:
            while dictionary[i] != 0:
                ans.append(i)
                dictionary[i] -= 1
                
        return ''.join(ans)
            
            
        