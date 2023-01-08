class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        
        numIndexPair = defaultdict(int)
        
        for index, val in enumerate(nums):
            numIndexPair[val] = index
            
        for i in range(len(operations)):
            numToReplace = operations[i][0]
            
            indexInNumsToReplace = numIndexPair[numToReplace]
            replacementElement =  operations[i][1] 
            nums[indexInNumsToReplace] =replacementElement
            
            numIndexPair[replacementElement] = indexInNumsToReplace
            del numIndexPair[numToReplace]
             
             
        return nums
