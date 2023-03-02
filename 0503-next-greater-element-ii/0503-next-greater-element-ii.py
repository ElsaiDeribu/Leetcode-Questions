class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        nums2 = [ i for i in range(len(nums))] * 2
        
        stack = []
        nxtGreatest = defaultdict(int)
        
        for idx in nums2:
            
            while stack and nums[stack[-1]] < nums[idx]:
                nxtGreatest[stack.pop()] = nums[idx]
                
            stack.append(idx)

        for i in range(len(nums)):
            nums[i] = nxtGreatest[i] if i in nxtGreatest else -1
            
        return nums