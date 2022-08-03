
class ListNode(object):
  def __init__(self, value=0,next=None):
    self.value = value
    self.next = next
class LinkedList:
  def __init__(self,value: int):
      self.value = value,
      self.next = None
      self.tail = self.head
      self.length = 1
  
  def append(self, value: int):
    new_node = ListNode(value, None)
    
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    return self
  
  def prepend(self, value: int): 
    new_node = ListNode(value, None)
    
    new_node.next = self.head
    self.head = new_node
    self.length += 1
    return self
  
  def printList(self):
    array = []
    current_node = self.head
    while current_node:
        array.append(current_node.value)
        current_node = current_node.next
    
    return array
  
  def insert(self, index: int, value: int):
    # Checkfor proper parameters
    if index >= self.length:
      print('yes')
      return self.append(value)
    
    
    new_node = ListNode(value, None)
    
    leader = self.traverseToIndex(self, index-1)
    holdingPointer = leader.next
    leader.next = new_node
    new_node.next = holdingPointer
    self.length += 1
    return self.printList()
  
  def traverseToIndex(self, index):
    # Checkparameters
    counter = 0
    current_node = self.head
    while counter != index:
      current_node = current_node.next
      counter += 1
    
    return current_node
  
  def remove(self, index: int):
    #Check Parameters      
    leader = self.traverseToIndex(self, index-1)
    unwanted_node = leader.next
    leader.next = unwanted_node.next
    self.length -= 1
    return self.printList()


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16).myLinkedList.prepend(1)
myLinkedList.insert(2, 99)
myLinkedList.insert(20, 88)
myLinkedList.remove(2)
