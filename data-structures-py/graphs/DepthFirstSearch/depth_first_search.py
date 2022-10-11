

class Node:
  def __init__(self, name):
    self.name = name
    self.children = []
  
  def add_child(self,name):
    self.children.append(Node(name))
    
  def depth_first_search(self,array):
    array.append(self.name)
    for child in self.children:
      child.depth_first_search(array)
    return array
