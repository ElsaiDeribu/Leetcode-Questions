class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        ans = set()
        nums.sort()
        
        for j in range(len(nums) - 3):
            if j == 0 or nums[i] != nums[j - 1]:
                
                for i in range( j + 1 , len(nums) - 2):

                    # if i == 1 or nums[i] != nums[i - 1]:

                        start = i + 1
                        end = len(nums)- 1

                        while start < end:

                            total = nums[j] + nums[i] + nums[start] + nums[end]

                            if total == target:

                                ans.add((nums[j], nums[i], nums[start], nums[end]))

                                # while start < end and nums[start] == nums[start + 1]: start += 1
                                # while start < end and nums[end]  == nums[end - 1]: end -= 1

                                start += 1
                                end -= 1

                            elif total > target: end -= 1
                            else: start += 1

        return list(ans)
                    
                        
                
            
        