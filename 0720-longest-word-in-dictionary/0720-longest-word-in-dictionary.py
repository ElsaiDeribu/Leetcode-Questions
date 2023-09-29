class TrieNode:
    
    def __init__ (self, char):
        self.char = char
        self.children = [0] * 26
        self.isEnding = False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = TrieNode("root")
        
        def add(word):
            nonlocal trie
            curr = trie
            
            for i in range(len(word)):
                idx = ord(word[i]) - 97
                
                if curr.children[idx] == 0:
                    curr.children[idx] = TrieNode(word[i])
                    
                curr = curr.children[idx]
                
            curr.isEnding = True
        
        for word in words:
            add(word)
           
        
        ans = []
        
        def dfs(curr, arr):
            nonlocal ans
                    
            for child in curr.children:
                if child != 0:  
                    if child.isEnding:
                        arr.append(child.char)
                        dfs(child, arr)
                        arr.pop() 
                        
                else:
                    if len(arr) > len(ans):
                        ans = arr[:]
                
        dfs(trie, [])   
        
        return ''.join(ans)
        
        
        
        
        
        
        
        
        