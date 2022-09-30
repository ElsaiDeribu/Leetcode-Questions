class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        length = len(nums)
        nums.extend(nums)
        
        ans = [-1] * length
        st = []
        
        for i in range(len(nums)):
            
            while st and st[-1][0] < nums[i]:
                
                if st[-1][1] < length:
                    ans[st[-1][1]] = nums[i]
                    
                st.pop()
            st.append((nums[i],i))
            
        return ans
        
            