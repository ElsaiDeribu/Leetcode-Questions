class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        forces = [0] * len(dominoes)
        f = 0
        ans = ""
        
        for i in range(len(dominoes)):
            
            if dominoes[i] == "R":
                f = len(dominoes)
            
            elif dominoes[i] == "L":
                f = 0
                
            else:
                f = max(f - 1, 0)
            
            forces[i] += f
        

        for j in range(len(dominoes) - 1, -1, -1):
            
            if dominoes[j] == "L":
                f = len(dominoes)
                
            elif dominoes[j] == "R":
                f = 0
                
            else:
                f = max(f - 1, 0)
                
            forces[j] -= f
                
        for i in forces:
            if i == 0:
                ans += "."
            elif i < 0:
                ans += "L"
            elif i > 0:
                ans += "R"
                
                
        return ans