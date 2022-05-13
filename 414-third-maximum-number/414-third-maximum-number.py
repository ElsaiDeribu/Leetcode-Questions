class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # O(n) Solution
        
        temp = set(nums)
        nums = list(temp)
        
        if len(nums) < 3:
            return max(nums)
        
        
        lst = []
        
        for i in range(len(nums)):
            lst.sort()
            if len(lst) < 3:
                lst.append(nums[i])      
            
            else:
                
                if nums[i] >= lst[-1]:
                    lst.pop(0)
                    lst.append(nums[i])
                elif nums[i] >= lst[-2]:
                    lst.pop(0)
                    lst.insert(1, nums[i])
                elif nums[i] >= lst[-3]:
                    lst[-3] = nums[i]
        lst.sort()
            
        return lst[0]
            
        
        
        
       ## O(nlogn) time complexity solution
    
#         dic = Counter(nums)

#         sorted_dic = sorted(dic.items(), key=lambda x: x[0])
        
#         if len(sorted_dic) < 3:
#             return max(dic)
        
#         else:
#             return sorted_dic[-3][0]
#         print(sorted_dic)
