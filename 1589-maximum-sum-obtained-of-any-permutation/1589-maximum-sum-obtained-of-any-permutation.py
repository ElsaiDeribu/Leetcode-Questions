class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        overlap = [0] * (len(nums) + 1)
        
        for request in requests:
            overlap[request[0]] += 1
            overlap[request[1] + 1] -= 1
            
        overlap = list(accumulate(overlap))
            
        nums.sort(reverse = True)
        overlap.sort(reverse = True)
        maxSum = 0

        for i in range(len(nums)):
            maxSum += (nums[i] * overlap[i])
        
        modulo =  10 ** 9 + 7
        
        return maxSum % modulo
            
        
        
            
        
        