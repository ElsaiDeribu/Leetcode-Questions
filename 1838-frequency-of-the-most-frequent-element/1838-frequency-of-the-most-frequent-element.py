class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        numbers = sorted(nums)
        i = 0
        j = 1
        freq= 0
        if len(nums) == 1:
            return 1
        sum = numbers[i] + numbers[j]
        while i < j:
            if((j-i+1)*numbers[j])-sum <=k:
                freq = max(freq, (j-i+1))
                if j < len(numbers) - 1:
                    j += 1
                    sum += numbers[j]
                    
                else:
                    break
            elif ((j-i+1)*numbers[j])-sum > k:
                    sum -= numbers[i]
                    i += 1
                                       
                    if j < len(numbers) - 1 and i == j:
                   
                        j += 1
                        sum += numbers[j]
                       
        if freq == 0:
            return 1
        
        return freq

        