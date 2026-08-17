class Solution:
    def HeightTree(self, root):
        if not root:
            return 0

        left_tree = root.left
        right_tree = root.right

        return max(self.HeightTree(left_tree), self.HeightTree(right_tree)) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

  
        if abs(self.HeightTree(root.left) - self.HeightTree(root.right)) > 1:
            return False

        left_tree = root.left
        right_tree = root.right
        
     
        return self.isBalanced(left_tree) and self.isBalanced(right_tree)