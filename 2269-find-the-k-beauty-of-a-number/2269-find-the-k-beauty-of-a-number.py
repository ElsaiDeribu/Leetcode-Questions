class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        num2 = str(num)
        count = l = 0
        r = k 
        
        while r < len(num2) + 1:
            candidate = int(num2[l:r])
            if candidate != 0 and not num % candidate:
                count += 1
            l += 1
            r += 1
        
        return count