class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        ans = []
        
        for i in count.keys():
            
            if count[i] > (len(nums)/3):
                ans.append(i)
                
        return ans
        