class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        cost = 0
        dicR = defaultdict(int)
        cnt = Counter()
        
        for i in range(len(instructions)):
            instructions[i] = (instructions[i], i)
            
        def divide(l, r):
            
            if l == r:
                return [instructions[r]]
            
            mid = l + (r - l) // 2
            
            left = divide(l, mid)
            right = divide(mid + 1, r)
            
            l = 0
            r = 0
            result = []
            while l < len(left) or r < len(right):
                
                if r >= len(right) or ( l < len(left) and left[l][0] <= right[r][0]):
                    result.append(left[l])
                    l += 1
                    
                else:
                    result.append(right[r])
                    dicR[right[r][1]] += len(left) - l
                    r += 1
                   
            return result
           
            
        divide(0, len(instructions) - 1)
        
        for i in range(len(instructions)):
            cost += min(i - dicR[i] - cnt[instructions[i][0]] , dicR[i])
            cost %= (10 ** 9 + 7)
            cnt[instructions[i][0]] += 1
                
        return cost 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # print(instructions)
        
#         def divide(arr):
            
#             if len(arr) <= 1:
#                 return arr
            
#             mid = len(arr) // 2
            
#             left = divide(arr[:mid])
#             right = divide(arr[mid:])
#             l = 0
#             r = 0
#             ptr = 0
#             # le = list(map(lambda x: x[0], left))
#             while l < len(left) or r < len(right):
                
#                 if r >= len(right) or ( l < len(left) and left[l][0] < right[r][0]):
#                     arr[ptr] = left[l]
#                     l += 1
#                     ptr += 1
                    
#                 else:
#                     arr[ptr] = right[r]
                    
#                     # rgt = bisect_right(left, right[r][0], key = lambda x: x[0])
                    
#                     dicR[right[r][1]] += len(left) - l
#                     dicL[right[r][1]] += l
                  
                    
#                     r += 1
#                     ptr += 1
                   
#             return arr
        
        
#         divide(instructions)
                    
                    