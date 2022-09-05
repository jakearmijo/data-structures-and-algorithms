class ListNode(object):
  def __init__(self, val=0,next=None):
    self.val = val
    self.next = next

class Soltuion:
  def remove_k_node_from_list(self, head: ListNode, n: int) -> ListNode:
      """
      type head: ListNode
      :type n: int
      :rtype: ListNode
      """
      # init dummy to use
      dummy = ListNode(0,head)
      # point left pointer at dummy 
      left = dummy
      # point right pointer at the head
      right = head
      # we are going to decrement n as we increase right until no n is left
      while n > 0 and right:
        # increment right to the next node value
        right = right.next
        # decrement n by 1 
        n -= 1

      # while right is not null.
      # update left point to the left next node 
      # update right pointer to the right next node
      while right:
        #these two pointers will now travel together
        # they are spaced out by n due to first while loop
        left = left.next
        right = right.next

      # when left stops it is at the node we want to remove
      # simply reassign this left node next value to skip the node we want to remove
      left.next = left.next.next

      # after all is complete the dummy node is on None and pointing to head.
      # if we right its .next value it will remove itself from start of list
      return dummy.next

