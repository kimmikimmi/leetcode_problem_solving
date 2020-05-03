'''
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root):
        q = [] 
        res =  []
        t = []
        if root is None:
            return res
        q.append(root)
        while q:
            t=[]  #empty list for each level
            level = len(q)
            while level != 0:
                temp = q.pop(0)
                level -= 1 
                t.append(temp.val)
                if temp.left:
                    q.append(temp.left) ###storing elemets of the tree level wise
                if temp.right:    
                    q.append(temp.right) ###storing elemets of the tree level wise
            res.append(t) ###final level stored in t
        return sum(t)