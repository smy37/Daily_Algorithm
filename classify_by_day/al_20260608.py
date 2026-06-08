# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete_node(cur, parent, b_first):
            if b_first:
                val = delete_node(cur.left, cur, False)
                return val
            else:
                if not cur.right:
                    if parent:
                        parent.right = None
                        return cur.val
                    return None
                else:
                    val = delete_node(cur.right, cur, False)
                    return val

        def update_root(node):
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:

                left_val = delete_node(node, None, True)
                node.val = left_val
                return node

        if root:
            if not root.left and not root.right and key == root.val:
                return None
            cur = root
            while cur:
                if cur.val == key:
                    update_root(cur)
                    break
                elif cur.val > key:
                    cur = cur.left
                elif cur.val < key:
                    cur = cur.right

        return root


