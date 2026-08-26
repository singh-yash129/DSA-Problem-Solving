class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Recursively process left and right subtrees first
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # If the current node becomes a leaf and matches the target, delete it by returning None
        if not root.left and not root.right and root.val == target:
            return None
            
        return root