# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #Find the length of the array
        n=len(lists)
        if(n==0):
            return None

        #Iterate through the array
        for i in range(0,n-1):
            mergedlist=self.merge(lists[i],lists[i+1])
            lists[i+1]=mergedlist

        return lists[n-1]

    def merge(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        #Create a dummy node
        dummy=ListNode()
        curr=dummy
        while(list1 and list2):
            if(list1.val<=list2.val):
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next

            curr=curr.next
        
        curr.next=list1 or list2
        return dummy.next