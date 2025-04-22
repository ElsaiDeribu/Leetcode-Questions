class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        l = 0
        r = len(arr) - 1
        
        while l + 1 < len(arr) and arr[l + 1] > arr[l]:
            l += 1

        while r - 1 >= 0 and arr[r - 1] > arr[r]:
            r -= 1

        if l == 0 or r == len(arr) - 1:
            return False
            
        return l == r