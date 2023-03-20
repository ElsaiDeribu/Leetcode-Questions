class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        total = 0
        spanLeft = defaultdict(lambda: -1)
        spanRight = defaultdict(lambda: len(arr))
        
        
        for i in range(len(arr)):
            
            while stack and arr[stack[-1]] >= arr[i]:
                
                temp = stack.pop()
                spanRight[temp] = i
                
            stack.append(i)
            
        
        for i in range(len(arr) - 1, -1, -1 ):
            
            while stack and arr[stack[-1]] > arr[i]:
                
                temp = stack.pop()
                spanLeft[temp] = i
                
            stack.append(i)
                
        for i in range(len(arr)):
            
            left = i - spanLeft[i] 
            right = spanRight[i] - i
            total += arr[i] * left * right

        modulo = 10**9 + 7
        
        return total % modulo