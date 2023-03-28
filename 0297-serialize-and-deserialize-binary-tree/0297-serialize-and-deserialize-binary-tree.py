# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        dic = defaultdict(int)
        
        
        def dfs(node, index):
            
            if not node:
                return
            
            dic[index] = node.val
            
            dfs(node.left, 2 * index)
            dfs(node.right, 2 * index + 1)
        
        dfs(root, 1)
        
        return json.dumps(dic)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # data = eval(data)
        data = json.loads(data)
        
        def build(index):
            
            if str(index) not in data:
                return
            
            node = TreeNode(data[str(index)])
            
            node.left = build(index * 2)
            node.right = build(index * 2 + 1)
            
            return node
        
        
        return build(1)
            
            
            
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))