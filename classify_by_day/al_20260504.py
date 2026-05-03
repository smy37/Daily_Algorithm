# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        val_list = []
        for node in lists:
            while node:
                val_list.append(node.val)
                node = node.next

        val_list.sort(reverse=True)

        cur = None
        for v in val_list:
            cur = ListNode(v, cur)

        return cur