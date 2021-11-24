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
        def serial(root):
            if not root:
                output.append('N')
                return
            
            output.append(str(root.val))
            
            serial(root.left)
            serial(root.right)
            
        output = []
        serial(root)
        
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serialized_tree = data.split(',')
        self.i = 0
        
        def deserial():
            if serialized_tree[self.i] == 'N':
                self.i += 1
                return
            
            root = TreeNode(int(serialized_tree[self.i]))
            self.i += 1
            
            root.left = deserial()
            root.right = deserial()
            
            return root
        
        
        return deserial()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))