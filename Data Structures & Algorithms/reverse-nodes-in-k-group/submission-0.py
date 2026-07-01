# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Create a dummy to point ot head
        dummy=ListNode(0,head)
        curr=dummy
        grpprev=dummy
        while(curr):
            #Get the value of current head
            chead=curr.next
            i=0
            while(i<k):
                    i+=1
                    curr=curr.next
                    if not curr:
                        return dummy.next
            
            #We traversed till k nodes so split the linked list
            grpnext=curr.next
            curr.next=None
            #Reverse from  head to curr and get new head
            rhead=self.reverse(chead)
            grpprev.next=rhead
            grpprev=chead
            #Post reversal we need to merge the head to rest of te linked list
            chead.next=grpnext
            curr=chead
        return dummy.next
    def reverse(self,head):
        prev=None
        curr=head
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
