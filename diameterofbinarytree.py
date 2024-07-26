from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the diameter if the path through the current node is longer
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter
