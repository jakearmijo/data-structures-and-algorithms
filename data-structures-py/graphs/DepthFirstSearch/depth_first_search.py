

class Node:
  def __init__(self, name):
    self.name = name
    self.children = []
  
  def add_child(self,name):
    self.children.append(Node(name))

# Write your code here.
# each node is a vertex - each line or connection is an edge
# Time = O(v + e)
# Space = O(v)
  def depth_first_search(self,array):
    array.append(self.name)
    for child in self.children:
      child.depth_first_search(array)
    return array
