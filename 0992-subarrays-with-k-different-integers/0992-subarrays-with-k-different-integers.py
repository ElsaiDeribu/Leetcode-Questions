class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(arr, maximum):
            
            dic = defaultdict(int)
            count = 0
            i = j = 0
            dic[nums[j]] = 1
            
            
            while j < len(nums):
                
                while len((dic)) > maximum:
                    dic[nums[i]] -= 1
                    if dic[nums[i]] == 0:
                        dic.pop(nums[i])
                    i += 1
                    
                count += (j - i + 1)
                j += 1
                if j < len(nums):
                    dic[nums[j]] += 1
            
            return count
        
        
        return helper(nums, k) - helper(nums, k - 1)
        
            