# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lst = []
        ptr = head
        
        while ptr:
            lst.append(ptr.val)
            ptr = ptr.next

        lst = self.mergeSort(lst)
        
        ptr = head
        for i in range(len(lst)):
            ptr.val = lst[i]
            ptr = ptr.next
            
        return head
        
    def mergeSort(self, arr):
        
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2 

        left = arr[:mid]
        right = arr[mid:]

        mergedLeft = self.mergeSort(left)
        mergedRight = self.mergeSort(right)

        lft = 0 
        rght = 0
        merged = 0

        while lft < len(mergedLeft) and rght < len(mergedRight):

            if mergedLeft[lft] > mergedRight[rght]:
                arr[merged] = mergedRight[rght]
                rght += 1

            else:
                arr[merged] = mergedLeft[lft]
                lft += 1
                
            merged += 1
            
        while  lft < len(mergedLeft):
            arr[merged] = mergedLeft[lft]
            lft += 1
            merged += 1

        while  rght < len(mergedRight):
            arr[merged] = mergedRight[rght]
            rght += 1
            merged += 1
            
        return arr

        