class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        start = 0
        def recursive (s, start, end):
            s[end],s[start] = s[start], s[end]
            end -= 1
            start += 1
            if end <= start:
                return s
            recursive (s, start, end)
            
            
        return recursive(s, start, end)