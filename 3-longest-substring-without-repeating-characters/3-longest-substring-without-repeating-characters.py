class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        largest = 0
        visited = defaultdict(int)
        while j < len(s):
            while j < len(s) and s[j] not in visited:
                visited[s[j]] = j
                j += 1
                largest = max(largest, j - i)

            if j < len(s):
                wantedPosition = visited[s[j]] + 1
                while i < wantedPosition:
                    del visited[s[i]]
                    i += 1

        return largest

        