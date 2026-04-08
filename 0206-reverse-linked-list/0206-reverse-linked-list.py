class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next   # store next node
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_temp        # move curr forward
        
        return prev