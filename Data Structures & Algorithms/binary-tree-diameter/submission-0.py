# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lengthBinaryTree(self, root):
        if not root:
            return 0
        left_root = root.left
        right_root = root.right

        return max(self.lengthBinaryTree(left_root), self.lengthBinaryTree(right_root))+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.lengthBinaryTree(root.left)
        rightHeight = self.lengthBinaryTree(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

        

        
        