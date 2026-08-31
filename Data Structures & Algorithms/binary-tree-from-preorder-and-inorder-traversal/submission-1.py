class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map inorder values to their indices for O(1) lookups
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        pre_idx = 0
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            # If there is no elements to construct subtrees
            if left > right:
                return None
            
            # The current root value from preorder traversal
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            
            # Split inorder index to divide left and right subtrees
            mid = inorder_idx[root_val]
            
            # Build left and right subtrees recursively
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
            
        return helper(0, len(inorder) - 1)