# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        extract_num = []

        def forward(cur):
            if cur.left:
                forward(cur.left)
            extract_num.append(cur.val)
            if cur.right:
                forward(cur.right)
        forward(root)
        extract_num.sort()
        
        cnt = 0
        def change_value(cur):
            nonlocal cnt
            if cur.left:
                change_value(cur.left)
            cur.val = extract_num[cnt]
            cnt += 1
            if cur.right:
                change_value(cur.right)

        change_value(root)
