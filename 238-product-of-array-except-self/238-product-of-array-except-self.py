class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProdList = []
        postProdList = [0] * len(nums)
        preProd = 1
        postProd = 1
        
        
        for i in range(len(nums)):
            preProd *= nums[i]
            preProdList.append(preProd)
        
        for j in range(len(nums) - 1, -1, -1):
            postProd *= nums[j]
            postProdList[j] = postProd
                
            
        for k in range (len(nums)):
            if k == 0:
                nums[k] = postProdList[k + 1]
                continue
            if k == len(nums) -1:
                nums[k] = preProdList[k - 1]
                break
            nums[k] = preProdList[k - 1] * postProdList[k + 1]
            
            
        return nums
            
            