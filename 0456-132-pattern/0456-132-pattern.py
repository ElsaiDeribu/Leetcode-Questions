class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        prevMin = float("inf")
        st = []
        
        for i in range(len(nums)):
            nums[i] = (nums[i], prevMin)
            prevMin = min(prevMin, nums[i][0])
            
        for i in range(len(nums) - 1, -1, -1):
            
            while st and st[-1] < nums[i][0]:
                if st[-1] > nums[i][1]:
                    return True
                st.pop()
                
            st.append(nums[i][0])
            
        return False