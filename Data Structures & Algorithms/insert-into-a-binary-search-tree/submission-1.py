class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If we reached an empty spot, create and return the new node wrapped in TreeNode
        if not root:
            return TreeNode(val)
        
        # Follow BST properties
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root