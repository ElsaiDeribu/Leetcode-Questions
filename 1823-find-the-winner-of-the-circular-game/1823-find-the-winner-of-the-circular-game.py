class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list = []
        for i in range(1,n+1):
            list.append(i)
        indexToRemove = 0
    
        def winner(list, k, indexToRemove):
            if len(list) == 1:
                return list[0]
            
            indexToRemove = (indexToRemove + k-1) % len(list)
                 
            if indexToRemove > len(list):
                indexToRemove = 0
                
            list.pop(indexToRemove)
                
            return winner(list, k , indexToRemove)
        
        return winner(list, k, indexToRemove)