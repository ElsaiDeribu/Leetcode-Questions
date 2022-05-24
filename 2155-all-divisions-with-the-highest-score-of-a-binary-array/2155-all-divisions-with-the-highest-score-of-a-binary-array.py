class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [0]
        postfix = [0]*(len(nums)+1)
        postfix[-1] = 0
        scores = defaultdict(list)
        
        maximum = 0
        counter = 0
        for i in range(len(nums) ):
            if nums[i] == 0:
                counter += 1
            prefix.append(counter)
            
            
        counter = 0   
        for i in range(len(nums)-1, -1,-1):
            if nums[i] == 1 :
                counter += 1
             
            postfix[i] = counter
            
        # print(prefix)
        # print(postfix)
        
        for i in range(len(nums) + 1):
            
            scores[(prefix[i] + postfix[i])].append(i)
            
            maximum = max(maximum, (prefix[i] + postfix[i]) )
            
        return scores[maximum]
            
        