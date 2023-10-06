class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [0] * 26
        self.end = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        trie = TrieNode("root")
        ans = 0
        
        def add(word):
            nonlocal trie
            curr = trie
            
            for i in range(len(word)):
                idx = ord(word[i]) - 97
                if curr.children[idx] == 0:
                    curr.children[idx] = TrieNode(word[i])
                curr = curr.children[idx]
                
            curr.end += 1
        
        for word in words:
            add(word)
          
        
        def dfs(curr, idx):
            nonlocal ans
            ans += curr.end
            flag = False
            for char in curr.children:
                if char != 0:
                    for i in range(idx, len(s)):
                        if s[i] == char.char:
                            flag = True
                            dfs(char, i + 1)
                            break
                            
        dfs(trie, 0)
        
        return ans
            
        
                    
            
            
            
            
            