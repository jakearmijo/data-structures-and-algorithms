
class ListNode(object):
  def __init__(self, val=0,next=None):
    self.val = val
    self.next = next

class Soltuion:
  def reorderLinkedList(self, head) -> None:
        """
        :type head: ListNode
        :rtype: None
        """
        # 2 pointers to iterate through
        # slow point and fast pointer
        slow, fast = head, head.next

        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

        # temp prev pointer to save link
        second = slow.next
        prev = None
        slow.next = prev

        while second:
          temp = second.next
          second.next = prev
          prev = second
          second = temp

        # merge two halves together
        first, second = head, prev

        while second:
          # temp 1 to store link 
          # temp 2 to store link
          temp1, temp2 = first.next, second.next
          first.next = second 
          second.next = temp1
          first, second = temp1, temp2
