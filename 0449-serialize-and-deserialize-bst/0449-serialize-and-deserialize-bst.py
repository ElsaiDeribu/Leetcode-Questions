# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        encoded = []
        
        def dfs(node):
            if not node:
                return
            
            encoded.append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return str(encoded)
            
            
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        
        data = eval(data)
                
        def build(arr):
            
            if not arr:
                return
            
            node = TreeNode(arr[0]) 
            
            splitIndex = len(arr)
            for i in range(1, len(arr)):
                if arr[i] > arr[0]:
                    splitIndex = i
                    break
                    
            node.left = build(arr[1:splitIndex])
            node.right = build(arr[splitIndex:])
            
            return node
        
        
        return build(data)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans