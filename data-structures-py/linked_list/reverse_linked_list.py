
class ListNode(object):
  def __init__(self, val=0,next=None):
    self.val = val
    self.next = next

class Soltuion:
  def reverseListIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
  
  def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        temp = head
        
        if head.next:
            temp = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None
        
        return temp