# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        global answer
        answer = 0

        def dfs(node):
            global answer
            cur = node
            cur_cnt = 0

            left_val = None
            right_val = None
            left_cnt = 0
            right_cnt = 0

            if cur.left:
                left_val, left_cnt = dfs(cur.left)
            if cur.right:
                right_val, right_cnt = dfs(cur.right)

            if cur.val == left_val and cur.val == right_val:
                answer = max(answer, left_cnt + right_cnt + 2)

            if cur.val == left_val:
                cur_cnt = max(cur_cnt, left_cnt + 1)
            if cur.val == right_val:
                cur_cnt = max(cur_cnt, right_cnt + 1)
            answer = max(answer, cur_cnt)

            return cur.val, cur_cnt

        if root:
            dfs(root)

        return answer