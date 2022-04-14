class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        removedElements = 0
        removedSize = 0
        H = len(arr)//2
        counts = Counter(arr)
        print(counts)
        for i, j in sorted(counts.items(), key=lambda k:k[1], reverse=True): 
            if removedSize >= H:
                break
            removedSize +=j
            removedElements += 1
        return removedElements