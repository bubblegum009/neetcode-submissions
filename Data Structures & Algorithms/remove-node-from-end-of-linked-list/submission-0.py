# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        l=0
        curr=head
        while(curr):
            l+=1
            curr=curr.next
        #Nth element form end is l-n element from front
        n=l-n
        dummyhead=ListNode()
        dummyhead.next=head
        curr=dummyhead
        curre=0
        while(curr):
            if(curre==n):
                curr.next=curr.next.next
                break
            curre=curre+1
            curr=curr.next
        return dummyhead.next

