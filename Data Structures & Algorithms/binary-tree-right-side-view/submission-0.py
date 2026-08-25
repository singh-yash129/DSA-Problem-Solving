class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
            
        queue = [root]
        
        while len(queue) > 0:
            level_length = len(queue)
            right_side_val = None
            
            for i in range(level_length):
                node = queue.pop(0)
                right_side_val = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(right_side_val)
            
        return res