class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        dic = Counter(nums)

        sorted_dic = sorted(dic.items(), key=lambda x: x[0])
        
        if len(sorted_dic) < 3:
            return max(dic)
        
        else:
            return sorted_dic[-3][0]
        print(sorted_dic)
