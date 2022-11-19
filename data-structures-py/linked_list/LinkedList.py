from tempfile import tempdir


class ListNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self,val:int) -> None:
    self.head = ListNode(val)
    self.tail = self.head
    self.length = 1
    print(f'init success ->{val} added -> new LL length {self.length} -> new head = {self.head.val} -> new tail {self.tail.val}')

  def append(self, val: int)-> None:
    new_node = ListNode(val)
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    print(f'append success -> {val} added -> new LL length {self.length} -> new tail {self.tail.val}')

    return self

  def prepend(self,val: int) -> None:
    new_node = ListNode(val)
    new_node.next = self.head
    self.head = new_node
    self.length += 1
    print(f'prepend success ->{val} added -> new LL length {self.length} -> new tail {self.tail.val}')
    return self;

  def insert(index: int, val: int) -> None:
    print('insert success');

my_ll = LinkedList(10)

my_ll.append(5)
my_ll.append(16)
my_ll.append(19)
my_ll.prepend(27)