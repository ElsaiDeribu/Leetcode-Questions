class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                j = 0
                k = i
                while j < k:
                    word[k], word[j] = word[j], word[k]
                    k -= 1
                    j += 1
                break
        
        
        return ''.join(word)