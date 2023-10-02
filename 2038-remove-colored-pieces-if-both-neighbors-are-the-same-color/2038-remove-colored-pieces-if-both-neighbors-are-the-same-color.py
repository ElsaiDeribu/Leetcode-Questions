class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        
        alice = 0
        bob = 0
        
        a = 0
        b = 0
        for i in range(len(colors)):
            if colors[i] == 'A':
                if a >= 2:
                    alice += 1

                b = 0
                a += 1
                
            if colors[i] == 'B':
                
                if b >= 2:
                    bob += 1
                
                a = 0
                b += 1
                
        
        return alice > bob
            