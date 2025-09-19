class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count = Counter(nums)
        ans = 0

        for num in list(count):
            target = k - num
            if target not in count:
                continue
            if num == target:
                ans += count[num] // 2
            else:
                ans += min(count[num], count[target])
            count[num] = 0
            count[target] = 0

        return ans
        