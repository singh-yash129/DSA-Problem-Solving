class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, the subtrees match
        if not p and not q:
            return True
        
        # If one node is None and the other is not, they don't match
        if not p or not q:
            return False
        
        # If the current values don't match, they aren't the same tree
        if p.val != q.val:
            return False
        
        # Recursively check both the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)