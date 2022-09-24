class ListNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.next = None
    self.prev = None

class DoubleLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = self.head
    self.length = 0



