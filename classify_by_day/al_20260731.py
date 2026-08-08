# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        num_list = []

        while head:
            num_list.append(head.val) 
            head = head.next

        if len(num_list) == 0: return None
        def make_tree(n_l: list):
            if len(n_l) == 1:
                return TreeNode(n_l[0])
            
            mid = len(n_l)//2

            left = n_l[:mid]
            right = n_l[mid+1:]
            left_tree, right_tree = None, None

            if left:
                left_tree = make_tree(left)

            if right:
                right_tree = make_tree(right)

            return TreeNode(n_l[mid], left_tree, right_tree)

        return make_tree(num_list)

