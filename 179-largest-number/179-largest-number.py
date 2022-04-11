class Solution(object):
    def largestNumber(self,  nums):
        flag = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                flag = 1;
        
        if flag == 0:
            return "0"
            
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                comb_1 = int(str(nums[i]) + str(nums[j]))
                comb_2 = int(str(nums[j]) + str(nums[i]))
                if comb_2 > comb_1:
                    nums[i],nums[j] = nums[j], nums[i]  

        nums = ''.join(map(str, nums))
 
        return nums
