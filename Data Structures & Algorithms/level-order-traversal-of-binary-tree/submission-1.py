class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def helper(node, level):
            if not node:
                return
            
            
            if len(res) == level:
                res.append([])
                
        
            res[level].append(node.val)
            
      
            helper(node.left, level + 1)
            helper(node.right, level + 1)
            
        helper(root, 0)
        return res