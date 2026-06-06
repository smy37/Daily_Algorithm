from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dq = deque()
        dq.append(root)

        while dq:
            cur = dq.popleft()
            if cur.val == val:
                return cur
            if cur.left:
                dq.append(cur.left)
            if cur.right:
                dq.append(cur.right)

        return None

