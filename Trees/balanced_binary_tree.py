# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        This is a modification of finding the height problem
        1. base case return null
        2. if left tree is not balanced return -1
        3. if right tree is not balanced return -1
        4. if height difference of left and right sub tree is > 1 return -1
        5. else return height
        '''
        def height(root):
            if not root:
                return 0
            leftheight = height(root.left)
            if leftheight == -1:
                return -1

            rightheight = height(root.right)
            if rightheight == -1:
                return -1
            
            if abs(leftheight - rightheight) > 1:
                return -1
            
            return max(leftheight,rightheight) + 1
        
        if height(root) == -1:
            return False
        else:
            return True