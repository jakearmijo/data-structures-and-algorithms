
class ListNode(object):
  def __init__(self, value=0,next=None):
    self.value = value
    self.next = next

class Solution:
  def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # init dummy point with a new ListNode
    dummy = ListNode()
    # set cur pointer to this dummy
    cur = dummy
    # init remainder for addition carry over
    remainder = 0

    # iterate through
    # remember to check all values - l1 or l2 or remainder
    while l1 or l2 or remainder:
      # basic addition but need to fill that empty space
      # Ex: 18+3=21 -> 8+3 = 11 -> 1 - carry the 1 -> remainder is 1 -> 1 + 0 + remainder
      # grab l1 val if it exist or 0
      val1 = l1.val if l1 else 0
      # grab l2 val if it exisit or 0
      val2 = l2.val if l2 else 0
      # add them together for new_sum
      new_sum = val1 + val2 + remainder
      # remainder is sliced off from sum // 10
      remainder = new_sum // 10
      # new sum must be single digit
      new_sum = new_sum % 10
      # insert into list a new node with this new_sum value
      cur.next = ListNode(new_sum)

      # update cur pointer
      cur = cur.next
      # update l1 pointer if it can else set it to null
      l1 = l1.next if l1 else None
      # update l2 pointer if it can else set it to null
      l2 = l2.next if l2 else None

    # after loop has complet dummy.next is pointing to our newly created and fille cur node
    return dummy.next
