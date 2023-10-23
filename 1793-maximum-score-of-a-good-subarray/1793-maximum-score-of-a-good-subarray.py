class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        st = []
        ranges = defaultdict(list)
        
        
        for i in range(len(nums) - 1, -1, -1):
            while st and nums[st[-1]] > nums[i]:
                num = st.pop()
                ranges[num].append(i + 1)
            
            st.append(i)
            
                
        for item in st:
            ranges[item].append(0)
            
        
        st = []
        
        for i in range(len(nums)):
            
            while st and nums[st[-1]] > nums[i]:
                num = st.pop()
                ranges[num].append(i - 1)
            
            st.append(i)
            
        
        for item in st:
            ranges[item].append(len(nums) - 1)
            
        
        ans = float("-inf")
            
        for element in ranges:
            
            left , right = ranges[element]
            idx = element
            
            if left <= k <= right:
                ans = max(ans, nums[idx] * (right- left + 1))
                
        return ans
        
        