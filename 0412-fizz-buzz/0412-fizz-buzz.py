class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1, n + 1):
            
            if not(i % 5) and not(i % 3):
                ans.append("FizzBuzz")
            
            elif not(i % 5):
                ans.append("Buzz")
            
            elif not(i % 3):
                ans.append("Fizz")
            
            else:
                ans.append(str(i))
                
        return ans