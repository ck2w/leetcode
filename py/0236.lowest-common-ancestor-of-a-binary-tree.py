#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (48.88%)
# Likes:    5368
# Dislikes: 201
# Total Accepted:    618.4K
# Total Submissions: 1.3M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 
# class Solution:
#     path1 = []
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         import copy
#         path_stack = []
#         node = root

#         def search_path(node, target):

#             if node.val == target.val:
#                 global path1
#                 path1 = copy.deepcopy(path_stack)
#                 return 0
#             if node.left:
#                 path_stack.append(node.left)
#                 search_path(node.left, target)
#                 path_stack.pop()
#             if node.right:
#                 path_stack.append(node.right)
#                 search_path(node.right, target)
#                 path_stack.pop()

#         search_path(node, p)
#         path_p = [root] + copy.deepcopy(path1)
#         search_path(node, q)
#         path_q = [root] + copy.deepcopy(path1)
        
#         for i in range(min(len(path_p), len(path_q))):
#             if path_p[i].val == path_q[i].val:
#                 continue
#             else:
#                 break
#         if path_p[i].val == path_q[i].val:
#             return path_p[i]
#         else:
#             return path_p[i-1]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
                
        
        s = set()  # p's parents
        while p:
            s.add(p)
            p = parent[p]
        
        while q not in s:            
            q = parent[q]
        
        return q


# @lc code=end

