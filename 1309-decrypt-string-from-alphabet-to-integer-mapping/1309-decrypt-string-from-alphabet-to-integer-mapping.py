class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        
        s = s.split("#")
        self.ans = ""
        print(s)
        
        def decrypt(l):
            for j in range(0, (len(s[l]) - 2)):
                self.ans += chr(int(s[l][j]) + 96)

            self.ans += chr(int(s[l][-2:]) + 96) 
                
        
        for i in range(len(s) - 1):
            decrypt(i)
            
        if not s[-1] == '':
            for i in range(len(s[-1])):
                print(i)
                print(s[-1][i])
                self.ans += chr(int(s[-1][i]) + 96)
            
            
        return self.ans
                
        