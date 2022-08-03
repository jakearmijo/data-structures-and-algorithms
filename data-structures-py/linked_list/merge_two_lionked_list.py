from logging.config import valid_ident
from typing import Optional

class ListNode(object):
  def __init__(self, val=0,next=None):
    self.val = val
    self.next = next

class Soltuion:
  def mergeTwoLinkedList(self, list1: Optional[ListNode], list2: Optional[ListNode]):
    """
    :type list: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype Optional[ListNode]
    """
    # init dummy node for tail ref
    dummy = ListNode()
    # set tail to this dummy
    tail = dummy
    # while list 1 and list 2 are not null
    while list1 and list2:
      #if the list 1 value is less than
      if list1.val < list2.val:
        # update tail.next ro list1
        tail.next = list1
        # update list1 to the list1 next node
        list1 = list1.next
      #else we are in list 2
      else:
        # update tail.next to list2
        tail.next = list2
        #update list 2 to 
        list2 = list2.next
      # no matter the condition we move tail to tail.next
      tail = tail.next

    # if list1 is not null move tail.next pointer to list1
    if list1:
      tail.next = list1
    # if list2 is not null move tail.next pointer to list2
    elif list2:
      tail.next = list2
    
    return dummy.next