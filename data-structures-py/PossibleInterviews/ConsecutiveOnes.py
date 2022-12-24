#  Given an integer, 
# count the maximum number of consecutive ones in its binary representation (e.g. 1011100000011 

class Solution:
  def consecutiveOnes(self, integer: int) -> int:

    if integer == 0:
      return 0

    string_of_int = str(integer)
    stack = []
    result = 0

    for x in string_of_int:
      int_of_string = int(x)
      if int_of_string == 1:
        stack.append(int_of_string)
        result = max(result,len(stack))
      else:
        stack = []

    return result


testing_Solution = Solution()

print('Test Case 1',testing_Solution.consecutiveOnes(1011100000011))
print('Test Case 2',testing_Solution.consecutiveOnes(111111111))
print('Test Case 3',testing_Solution.consecutiveOnes(1))
print('Test Case 4',testing_Solution.consecutiveOnes(000000000000))
print('Test Case 5',testing_Solution.consecutiveOnes(0))
print('Test Case 6',testing_Solution.consecutiveOnes(111101001111100011))
