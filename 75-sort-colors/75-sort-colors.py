class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr