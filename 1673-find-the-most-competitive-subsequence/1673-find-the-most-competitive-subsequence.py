class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        st = []
        
        for i in range(len(nums)):
            while st and st[-1] > nums[i] and len(st) + len(nums) - i > k:
                st.pop()
             
            if len(st) < k:
                st.append(nums[i])
        
        return st