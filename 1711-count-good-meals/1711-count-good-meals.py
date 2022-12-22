class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        dic = defaultdict(int)
        count = 0
        
        for i in range(len(deliciousness)):
            for j in range(22):
                temp = (2**j) - deliciousness[i] 
                if temp in dic:
                    count += dic[temp]
            dic[deliciousness[i]] += 1
                    
        
        return count % ((10**9) + 7)
        