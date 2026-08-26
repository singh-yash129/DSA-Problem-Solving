class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize to negative infinity to handle trees with all negative values
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Compute the max path sum from left and right children.
            # We use max(0, ...) to ignore paths with negative sums.
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            # Price of the path containing the current node as the "highest" node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the max sum of a path extending to the parent (current node + max of one branch)
            return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return self.max_sum