class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        
        count = Counter(nums)
        
        count = sorted(count.items(), key = lambda x : x[0]) 
        
        dic = defaultdict(int)
        
        sumTillNow = 0
        
        for i in range(len(count)):
            dic[count[i][0]] = sumTillNow
            sumTillNow += count[i][1]
        
        
        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        
        return nums
        
        
        
        
#         output = [0] * len(nums)
#         check = []
        
#         sort = sorted(nums)
#         for i in range(len(nums)):
#             if sort[i] in check:
#                 output.pop()
#                 continue
#             else:
#                 output[i] = i
#                 check.append(sort[i])
#         return output
                