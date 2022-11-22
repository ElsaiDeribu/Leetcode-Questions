class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowElements = deque([])
        ans = []
        l = 0
        for r in range(len(nums)):
            while r - l + 1 > k:
                if nums[l] == windowElements[0]:
                    windowElements.popleft()
                l += 1
            
            while windowElements and windowElements[-1] < nums[r]:
                windowElements.pop()
            windowElements.append(nums[r])
            
            if r - l + 1 == k:
                ans.append(windowElements[0])
            
        return ans