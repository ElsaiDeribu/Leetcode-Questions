class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        st = []
        currMin = nums[0]
        
        for num in nums:
            
            while st and st[-1][-1] <= num:
                st.pop()
                
            if st and st[-1][0] < num:
                return True
            
            currMin = min(currMin, num)
            st.append([currMin, num])
            
            
        return False
            
        