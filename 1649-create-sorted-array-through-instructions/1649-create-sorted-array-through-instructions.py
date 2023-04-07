class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        cost = 0
        dicR = defaultdict(int)
        cnt = Counter()
        
            
        def divide(l, r):
            
            if l == r:
                return [r]
            
            mid = l + (r - l) // 2
            
            left = divide(l, mid)
            right = divide(mid + 1, r)
            
            l = 0
            r = 0
            result = []
            while l < len(left) or r < len(right):
                
                if r >= len(right) or ( l < len(left) and instructions[left[l]] <= instructions[right[r]]):
                    result.append(left[l])
                    l += 1
                    
                else:
                    result.append(right[r])
                    dicR[right[r]] += len(left) - l
                    r += 1
                   
            return result
           
            
        divide(0, len(instructions) - 1)
        
        for i in range(len(instructions)):
            cost += min(i - dicR[i] - cnt[instructions[i]] , dicR[i])
            cost %= (10 ** 9 + 7)
            cnt[instructions[i]] += 1
                
        return cost 
            
