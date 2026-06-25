class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
           
            left_valid = valid(node.left, low, node.val)
            right_valid = valid(node.right, node.val, high)
            
            return left_valid and right_valid
        
        return valid(root, float('-inf'), float('inf'))
