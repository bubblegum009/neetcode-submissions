"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Start of new List
        newNode=Node(0)
        #List to map the random pointer values
        rp={}
        curr=head
        prev=newNode
        while(curr):
            #Create New Node
            cnewnode=Node(curr.val)
            #Map thecurrent node to new node
            rp[curr]=cnewnode
            #Attach new node to previous
            prev.next=cnewnode
            #Update previous node
            prev=cnewnode
            curr=curr.next

        cur1=head
        cur2=newNode.next
        while(cur1):
            rpval=cur1.random
            cur2.random=rp.get(rpval,None)
            cur1=cur1.next
            cur2=cur2.next
        
        return newNode.next