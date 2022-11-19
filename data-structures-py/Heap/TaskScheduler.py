# 621. Task scheduler

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

 

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.


# Example 2:
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

# Example 3:
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

# Constraints:
# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].

import heapq
import Counter
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

      # counter() creates hash map of key and values
      count = Counter(tasks)
      # no max heap in python so need negative
      maxHeap = [-cnt for cnt in count.values()]
      # heapify is O(n) time
      heapq.heapify(maxHeap)
      # init time variable to track each instance of time to return
      time = 0
      # init que to push each value to track
      # double ended que will contain a pair of values [-cnt, idleTime]
      q = collections.deque()

      while maxHeap or q:
        # increment time cause you are on new task
        time += 1

        if maxHeap:
        # when the max heap is non empty we pop
          cnt = 1 + heapq.heappop(maxHeap)
        # we are now processing a task add 1 to the cnt to subtract 1
          if cnt:
            q.append([cnt,time + n])

        if q and q[0][1] == time:
          heapq.heappush(maxHeap, q.popleft()[0])

      return time
        

