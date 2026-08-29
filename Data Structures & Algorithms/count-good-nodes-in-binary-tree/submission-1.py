class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # A node is good if its value is greater than or equal to the max value on the path
            count = 1 if node.val >= max_val else 0
            
            # Update the max value for the children paths
            current_max = max(max_val, node.val)
            
            # Recursively check left and right subtrees
            count += dfs(node.left, current_max)
            count += dfs(node.right, current_max)
            
            return count

        # Start DFS with the root value as the initial maximum
        return dfs(root, root.val)