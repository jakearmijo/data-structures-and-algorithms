
class ListNode(object):
  def __init__(self, value=0,next=None):
    self.value = value
    self.next = next

# Floyd Tortoise and Hare

# time = O(n) space = O(1)
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    # init slow and fast pointers
    slow, fast = head, head
    # while there is a fast pointer and fast.next pointer
    while fast and fast.next:
      # increase slow by 1 and fast by 2
      slow = slow.next
      fast = fast.next.next
      # if these pointers meet there is a cycle
      if slow == fast:
        return True
    
    return False


