class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count = Counter(nums)
        
        for i in count.keys():
            if count[i] >= 2:
                return True
            
        return False
        