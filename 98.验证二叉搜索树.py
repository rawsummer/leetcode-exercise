#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution:
    def isValidBSTReal(self,root:TreeNode,min:TreeNode,max:TreeNode):
        if root == None:
            return True
        
        if (min != None and root.val <= min.val):
            return False
        if (max != None and root.val >= max.val):
            return False

        return self.isValidBSTReal(root.left,min,root) and self.isValidBSTReal(root.right,root,max)
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTReal(root,None,None)

# @lc code=end

