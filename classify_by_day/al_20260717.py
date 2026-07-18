# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        num_list_left = []
        num_list_right = []

        cur = head
        while cur:
            if cur.val < x:
                num_list_left.append(cur.val)
            else:
                num_list_right.append(cur.val)

            cur = cur.next

        cur = None

        for i in range(len(num_list_right)-1, -1, -1):
            cur = ListNode(num_list_right[i], cur)

        for i in range(len(num_list_left)-1, -1, -1):
            cur = ListNode(num_list_left[i], cur)

        return cur
