
class ListNode(object):
  def __init__(self, x: int,next=None, random=None):
    self.value = int(x)
    self.next = next
    self.random = random

class Solution:
  def copy_list(self, head):
    """
    :type head: ListNode
    :rtype: None
    """
    # init hashmap to create copyes of nodes
    # in order to return at end we will need to have a stopping point
    # LL stopping point is usually a null value
    old_nodes = { None: None }
    # set current point to iterate with starting at head
    cur = head
    # while cur is not null
    while cur:
      # create a COPY of this node's value
      copy = ListNode(cur.value)
      # map into hash map
      old_nodes[cur] = copy
      # move pointer along
      cur = cur.next

    # reset cur point for 2nd pass
    cur = head
    # while cur is not null
    while cur:
      # reference hash map to find cur then assign the 2 properties
      copy_of_cur = old_nodes[cur]
      copy_of_cur.next = old_nodes[cur.next]
      copy_of_cur.random = old_nodes[cur.random]
      # move pointer along
      cur = cur.next

    # after comple can return the refernce copy of head from hash map
    return old_nodes[head]
