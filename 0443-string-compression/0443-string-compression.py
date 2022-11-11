class Solution:
    def compress(self, chars: List[str]) -> int:
        
        char2 = []
        count = 0
        
        l = 0
        r = 0
        
        while r < len(chars):
            while r < len(chars) and chars[r] == chars[l]:
                count += 1
                r += 1
                
            char2.append(chars[l])
            if count > 1:
                temp = str(count)
                for i in temp:
                    char2.append(i)
            count = 0
            l = r
                
        for i in range(len(char2)):
            chars[i] = char2[i]
        
        
        while len(chars) != len(char2):
            chars.pop()
            
        
        