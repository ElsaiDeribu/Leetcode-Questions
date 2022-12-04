class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        
        even = sorted(Counter(list(filter(lambda x: x % 2 == 0, nums))).items(), key = lambda x: x[1])
        evenTie = sorted(list(filter(lambda x: x[1] == even[-1][1], even)))
        
        return evenTie[0][0] if even else -1     
                
        
        