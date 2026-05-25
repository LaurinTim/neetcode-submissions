# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        dummy = ListNode()
        new = dummy 

        while list1 and list2: 
            if list1.val <= list2.val: 
                new.next = list1 
                list1 = list1.next 
            else: 
                new.next = list2
                list2 = list2.next 
            new = new.next 
        
        new.next = list1 if list1 else list2

        return dummy.next 