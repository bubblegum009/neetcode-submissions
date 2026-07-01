# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
           return head
        #Have pointers to store the current and previous value
        #Each nodes know only ablut their next value
        curr=head
        prev=None
        while curr:
            #Preserve the future fl0w of lists
            temp=curr.next
            #Link current to prev
            curr.next=prev
            prev=curr
            curr=temp

        return prev


