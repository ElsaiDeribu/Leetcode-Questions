class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest = 10**4 + 1
        ans = None
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            if i == 0 or nums[i - 1] != nums[i]:
            
                l = i + 1

                r = len(nums) - 1


                while l < r:

                    total = nums[i] + nums[l] + nums[r]

                    if total > target:

                        if abs(total - target ) < closest:

                            ans = total
                            closest =  abs(total - target )

                        # while l < r and nums[r - 1] == nums[r]: 
                        r -= 1


                    elif total < target:

                         if abs(total - target ) < closest:

                            ans = total
                            closest =  abs(total - target )

                         # while l < r and nums[l] == nums[l + 1]:
                         l += 1

                    else:

                        return total

                    
        return ans
                    
            
            
        