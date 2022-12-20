class Solution:
    def average(self, salary: List[int]) -> float:
        
        maximum = float("-inf")
        minimum = float("inf")
        
        total = 0
        for i in range(len(salary)):
            total += salary[i]
            
            maximum = max(maximum, salary[i])
            minimum = min(minimum, salary[i])
            
        return (total - (maximum + minimum)) / (len(salary) - 2)