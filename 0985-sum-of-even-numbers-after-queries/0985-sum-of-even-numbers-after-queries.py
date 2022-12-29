class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        sum_of_even = 0
        
        for i in nums:
            if i % 2 == 0:
                sum_of_even += i
        
        for q in queries:
            
            if nums[q[1]] % 2 == 0:
                if q[0] % 2 == 0:
                    sum_of_even += q[0]
                else:
                    sum_of_even -= nums[q[1]]
                nums[q[1]] += q[0]
                
            elif nums[q[1]] % 2 != 0:
                
                if q[0] % 2 != 0:
                    sum_of_even += (nums[q[1]] + q[0])
                nums[q[1]] += q[0]

            ans.append(sum_of_even) 
            
        return ans