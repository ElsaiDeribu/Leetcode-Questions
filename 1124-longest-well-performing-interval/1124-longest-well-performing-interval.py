class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        prefixes = defaultdict(int)
        # prefixes[0] = -1
        sumUpToNow = 0
        longest = 0
        
        for i in range(len(hours)):
            sumUpToNow += (1 if hours[i] > 8 else -1) 
            if sumUpToNow > 0:
                longest = max(longest, i + 1)
            elif sumUpToNow - 1 in prefixes:
                longest = max(longest, i - prefixes[sumUpToNow - 1])
            if sumUpToNow not in prefixes:
                prefixes[sumUpToNow] = i

        return longest