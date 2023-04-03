class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
                   
        distinct = set()
        
        def addPrimeFactorsOf(num):
            
            d = 2

            while d * d <= num:

                while num % d == 0:
                    distinct.add(d)
                    num //= d

                d += 1

            if num != 1:
                distinct.add(num)

     
        for num in nums:
            addPrimeFactorsOf(num)
        
        
        return len(distinct)
