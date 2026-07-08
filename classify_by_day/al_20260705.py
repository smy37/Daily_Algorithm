from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        answer = []
        def dfs(cur_node, record):
            if cur_node.left is None and cur_node.right is None:
                record = record + [cur_node.val]
                if sum(record) == targetSum:
                    answer.append(record)
            else:
                if cur_node.left is not None:
                    dfs(cur_node.left, record+[cur_node.val])
                if cur_node.right is not None:
                    dfs(cur_node.right, record+[cur_node.val])
        if root is not None:
            dfs(root, [])
        return answer



        
