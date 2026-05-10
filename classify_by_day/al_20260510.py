# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = []
        node_2 = []

        if list1:
            cur = list1.val
            node_1.append(cur)
            while list1.next:
                list1 = list1.next
                cur = list1.val
                node_1.append(cur)

        if list2:
            cur = list2.val
            node_2.append(cur)
            while list2.next:
                list2 = list2.next
                cur = list2.val
                node_2.append(cur)

        sorted_node = sorted(node_1 + node_2, reverse=True)

        cur = None

        for v in sorted_node:
            cur = ListNode(v, cur)

        return cur