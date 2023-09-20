class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
                 
        pref = nums[:]
        post = nums[:]
        
        for i in range(1, len(pref)):
            pref[i] += pref[i - 1] 
            
        for i in range(len(pref) - 2, -1, -1):
            post[i] += post[i + 1]
        
        post.append(0)
        post = post[::-1]
        
        temp = [0]
        temp.extend(pref)
        pref = temp
       
        ans = float("inf")
        
        for i in range(len(nums)):
            req = x - pref[i] 
            possIdx = bisect_left(post, req)
            
            if possIdx < len(post) and (possIdx + i) < len(post) and post[possIdx] == req:
                ans = min(ans, i + possIdx)
                
            
        return ans if ans != float("inf") else -1


        
        