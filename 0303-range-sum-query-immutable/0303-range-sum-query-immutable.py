class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = nums
        
        for i in range(1, len(nums)):
            self.prefixes[i] = self.prefixes[i - 1] + self.prefixes[i]
        
    def sumRange(self, left: int, right: int) -> int: 
            
        return self.prefixes[right] - self.prefixes[left - 1] if left else  self.prefixes[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)