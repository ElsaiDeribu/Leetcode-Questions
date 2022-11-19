class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        for i in range(len(hours)):
            if hours[i] > 8:
                hours[i] = 1
            else:
                hours[i] = -1
        
        # print(hours)
        prefixes = defaultdict(int)
        prefixes[0] = -1
        sumUpToNow = 0
        longest = 0
        
        for i in range(len(hours)):
            sumUpToNow += hours[i]
            # print(sumUpToNow, i)
            if sumUpToNow > 0:
                longest = max(longest, i + 1)
            elif sumUpToNow - 1 in prefixes:
                if i - prefixes[sumUpToNow - 1] >  longest:
                    longest = i - prefixes[sumUpToNow - 1]
            if sumUpToNow not in prefixes:
                prefixes[sumUpToNow] = i
            # print(prefixes)
            

        return longest