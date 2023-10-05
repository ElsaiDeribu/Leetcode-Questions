class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = []
        count = Counter(nums)
        
        for num in count:
            if count[num] > len(nums) / 3:
                ans.append(num)
                
        return ans
        