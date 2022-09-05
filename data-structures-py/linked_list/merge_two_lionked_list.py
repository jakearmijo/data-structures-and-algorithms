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
    # init dummy node for temp ref
    dummy = ListNode()
    # set temp to this dummy
    temp = dummy
    # while list 1 and list 2 are not null
    while list1 and list2:
      #if the list 1 value is less than
      if list1.val < list2.val:
        # update temp.next ro list1
        temp.next = list1
        # update list1 to the list1 next node
        list1 = list1.next
      #else we are in list 2
      else:
        # update temp.next to list2
        temp.next = list2
        #update list 2 to 
        list2 = list2.next
      # no matter the condition we move temp to temp.next
      temp = temp.next

    # if list1 is not null move temp.next pointer to list1
    if list1:
      temp.next = list1
    # if list2 is not null move temp.next pointer to list2
    elif list2:
      temp.next = list2
    
    return dummy.next