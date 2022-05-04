class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        i = 0
        j = 1
        ans = []
        while j < len(chars):
            if chars[i] == chars[j]:
                counter += 1
                if j + 1 < len(chars) and chars[j + 1] != chars[j]:
                    chars[j] = str(counter)
                    j += 2
                    i += 2
                    counter = 1
                    continue
                if j + 1 >= len(chars) :
                    chars[j]  = str(counter)
                    break

                chars.pop(j)
            else:
                j += 1
                i += 1

        i = 0
        while i < len(chars):
            if len(chars[i]) > 1:
                for j in chars[i]:
                    ans.append(j)
                i += 1
            if i < len(chars):
                ans.append(chars[i])
                i += 1
        for i in range(len(ans)):
            if i >= len(chars):
                chars.append(ans[i])
            else:
                chars[i] = ans[i]
        
        
        return len(chars)
