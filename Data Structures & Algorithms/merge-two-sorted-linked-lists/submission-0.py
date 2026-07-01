# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        newList=ListNode()
        dummyhead=newList
        while(list1 and list2):
            while(list1 and list2 and list1.val <= list2.val):
                newList.next=list1
                newList=newList.next
                list1=list1.next
            while(list1 and list2 and list2.val < list1.val):
                newList.next=list2
                newList=newList.next
                list2=list2.next
        if list1:
            newList.next=list1
        elif list2:
            newList.next=list2
        return dummyhead.next
