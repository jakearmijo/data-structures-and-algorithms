# Problem: Implement a min heap with extract_min and insert methods.
# Constraints
# Can we assume the inputs are ints?
# Yes
# Can we assume this fits memory?
# Yes

# Test Cases:
# Extract min of an empty tree
# Extract min general case
# Insert into an empty tree
# Insert general case (left and right insert)
#           _5_

#         /     \

#        20     15

#       / \    /  \

#      22  40 25

# extract_min(): 5
#           _15_

#         /      \

#        20      25

#       / \     /  \

#      22  40 

# insert(2):
#           _2_

#         /     \

#        20      5

#       / \     / \

#      22  40  25  15

# Algorithm:
# A heap is a complete binary tree where each node is smaller than its children.

# extract_min
#           _5_

#         /     \

#        20     15

#       / \    /  \

#      22  40 25

# Save the root as the value to be returned: 5
# Move the right most element to the root: 25
#           _25_

#         /      \

#        20      15

#       / \     /  \

#      22  40 



# Bubble down 25: Swap 25 and 15 (the smaller child)



#           _15_

#         /      \

#        20      25

#       / \     /  \

#      22  40 



# Return 5



# We'll use an array to represent the tree, here are the indices:



#           _0_

#         /     \

#        1       2

#       / \     / \

#      3   4   



# To get to a child, we take 2 index + 1 (left child) or 2 index + 2 (right child).



# For example, the right child of index 1 is 2 * 1 + 2 = 4.





#           _5_

#         /     \

#        20     15

#       / \    /  \

#      22  40 25

# insert(2):
# Insert at the right-most spot to maintain the heap property.

#           _5_

#         /     \

#        20     15

#       / \    /  \

#      22  40 25   2

# Bubble up 2: Swap 2 and 15
#           _5_

#         /     \

#        20     2

#       / \    / \

#      22  40 25  15

# Bubble up 2: Swap 2 and 5
#           _2_

#         /     \

#        20     5

#       / \    / \

#      22  40 25  15

# We'll use an array to represent the tree, here are the indices:
#           _0_

#         /     \

#        1       2

#       / \     / \

#      3   4   5   6

# To get to a parent, we take (index - 1) // 2.
# For example, the parent of index 6 is (6 - 1) // 2 = 2.

class MinHeap():
  def __init__(self) -> None:
    self.array = []
  
  def __len__(self) -> int:
    return len(self.array)

  def extract_min(self) -> int:
    if not self.array:
      return None
    if len(self.array) == 1:
      return self.array.pop(0)
    # set min before bubbling
    minimum = self.array[0]
    # Move the last element to the root
    # bubbling will redistribute elements
    self.array[0] = self.array.pop(-1)
    self.bubble_down(index=0)
    # return min after bubble
    return minimum
  
  def peek_min(self) -> int:
    return self.array[0] if self.array else None

  def insert(self, val: int) -> None:
    if val is None:
      raise TypeError(' Can not insert None val')
    self.array.append(val)
    self.array.bubble_up(index=len(self.array) - 1)

  def bubble_up(self, index) -> None:
    if index == 0:
      return
    index_parent = (index - 1) // 2
    # if cur element is less than parent element
    if self.array[index] < self.array[index_parent]:
      # Swap the indices and recurse
      self.array[index], self.array[index_parent] = self.array[index_parent], self.array[index]
      self.bubble_up(index_parent)

  def bubble_down(self, index) -> None:
    min_child_index = self.find_smaller_child(index)
    if min_child_index == -1:
      return
    if self.array[index] > self.array[min_child_index]:
      # Swap the indices and recurse
      self.array[index], self.array[min_child_index] = self.array[min_child_index], self.array[index]
      self.bubble_down(min_child_index)
  
  def find_smaller_child(self, index) -> int:
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    # No right child
    if right_child_index >= len(self.array):
      # No Left Child
      if left_child_index < len(self.array):
        return -1
      # Left Child Only
      else:
        return left_child_index
    else:
      # Compare left and right children
      if self.array[left_child_index] < self.array[right_child_index]:
        return left_child_index
      else:
        return right_child_index


# Complexity:
# Time: O(lg(n))
# Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach
# insert