# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow=head
        fast=head
        #Find the middle element
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        
        #Reverse the second half
        prev=None
        curr=slow.next
        #Split the first half
        slow.next=None
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        #Merge list from head and prev
        curr=head
        while(prev):
            temp1=curr.next
            temp2=prev.next
            curr.next=prev
            prev.next=temp1
            curr=temp1
            prev=temp2
            

    

        
        
