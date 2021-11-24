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
        def dfs(root):
            if not root:
                output.append('N')
                return
            
            output.append(str(root.val))
            
            dfs(root.left)
            dfs(root.right)
            
        output = []
        dfs(root)
        
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serial_data = data.split(',')
        self.i = 0
        
        def dfs():
            if serial_data[self.i] == 'N':
                self.i += 1
                return
                
            root = TreeNode(int(serial_data[self.i]))
            self.i += 1
            
            root.left = dfs()
            root.right = dfs()
            
            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))