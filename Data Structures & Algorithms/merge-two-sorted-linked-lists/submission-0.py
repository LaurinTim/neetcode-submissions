# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        curr1 = list1
        curr2 = list2
        
        if list1.val <= list2.val:
            head = list1
            curr = list1
            curr1 = list1.next
        else:
            head = list2
            curr = list2
            curr2 = list2.next

        while curr1 or curr2:
            if not curr1:
                curr.next = curr2
                return head
            elif not curr2:
                curr.next = curr1
                return head
            
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
            
        return head
            

        