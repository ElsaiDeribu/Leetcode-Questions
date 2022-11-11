class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newIndexValPair  = [] 
        n = len(nums)
        for i in range(len(nums)):
            newIndexValPair.append(((i + k) % n, nums[i]))
            
        for i in newIndexValPair:
            nums[i[0]] = i[1]
            
            
            
        