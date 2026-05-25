# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        elif len(lists) == 1:
            return lists[0]
        else:
            lists = [lists[0], self.mergeKLists(lists[1:])]
        dummy = ListNode()
        curr = dummy
        curr1 = lists[0]
        curr2 = lists[1]
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next
        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2
        return dummy.next
        
        