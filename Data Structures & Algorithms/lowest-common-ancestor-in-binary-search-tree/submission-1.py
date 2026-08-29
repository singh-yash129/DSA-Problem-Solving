class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        # Check if root value is between p and q values (inclusive)
        if p.val <= root.val and root.val <= q.val or q.val <= root.val and root.val <= p.val:
            return root

        # Traverse left or right based on values
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)