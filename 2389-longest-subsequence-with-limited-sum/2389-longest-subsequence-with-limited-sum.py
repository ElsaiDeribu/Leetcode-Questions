class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        print(nums)
        
        for i in range(len(queries)):
            l = 0
            sumation = nums[l]
            while sumation <= queries[i] and l < len(nums):
                l += 1
                if l < len(nums):
                    sumation += nums[l]
            ans.append(len(nums[:l]))
            
        return ans