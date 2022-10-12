class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix = [0] * (len(s) + 1)
        ans = []
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for i in shifts:
            
            if i[2] == 0:
                prefix[i[0]] -= 1
                prefix[i[1] + 1] += 1
            else:
                prefix[i[0]] += 1
                prefix[i[1] + 1] -= 1
                
        for i in range(1,len(prefix)):
            
            prefix[i] += prefix[i - 1]
            
            
        for i in range(len(prefix) - 1):
        
            ans.append(letters[(letters.index(s[i]) + prefix[i]) % 26])
                
                       
        return ''.join(ans)