class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]


        head = 0
        while head != slow:
            slow = nums[slow]
            head = nums[head]

        return head
            