# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Newlist=ListNode()
        prev=Newlist

        #Store the head of l1 and l2
        l1head=l1
        l2head=l2

        #Store the remainder
        r=0
        while l1head or l2head:
            val1=l1head.val if l1head else 0
            val2=l2head.val if l2head else 0
            add=val1+val2+r
            r=add//10
            newval=add%10
            newnode=ListNode(newval)
            prev.next=newnode
            prev=newnode
            #Iterate the lists:
            l1head=l1head.next if l1head else l1head
            l2head=l2head.next if l2head else l2head

        #Check if last addition lead to a remainder
        if(r>0):
            newNode=ListNode(r)
            prev.next=newNode

        return Newlist.next
