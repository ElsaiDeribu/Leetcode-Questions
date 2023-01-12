class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        people = []
        
        for i in range(1, n + 1):
            people.append(i)
        
        indexToRemove = 0
        
        while len(people) > 1:
            
            indexToRemove = (indexToRemove + k - 1) % len(people)
            people.pop(indexToRemove)
         
        return people[0]
            
            
            
            

        
      

            
            
        
        