## Given two strings Write a method to decide if one is a permutation of the other

## permutation = a way, especially one of several possible variations, 
# in which a set or number of things can be ordered or arranged.



# solution One - sort the strings and check if they are the same
class SolutionOne:
  def checkPermutation(self, string_one: str, string_two: str) -> bool:

    if len(string_one) != len(string_two):
      return False

    sorted_one = sorted(string_one)
    sorted_two = sorted(string_two)

    if sorted_one == sorted_two:
      return True
    else:
      return False

#Solution Two - 
class SolutionTwo:
  def checkPermutation(self, string_one: str, string_two: str) -> bool:

    if len(string_one) != len(string_two):
      return False
    
    hash_one = {}

    for char in string_one:
      hash_one[char] = 1 + hash_one.get(char, 0)
    hash_one[char] += 1
    
    for char in string_two:
      if char not in hash_one:
        return False
      else:
        hash_one[char] -= 1

    return True



testing_solution_one = SolutionOne()
print('testing_solution_one -> ',testing_solution_one.checkPermutation(string_one='abcd', string_two='bacd'))
print('testing_solution_one -> ',testing_solution_one.checkPermutation(string_one='3563476', string_two='7334566'))
print('testing_solution_one -> ',testing_solution_one.checkPermutation(string_one='wef34f', string_two='wffe34'))
print('testing_solution_one -> ',testing_solution_one.checkPermutation(string_one='abcd', string_two='d2cba'))
print('testing_solution_one -> ',testing_solution_one.checkPermutation(string_one='2354', string_two='1234'))
print('testing_solution_one -> ',testing_solution_one.checkPermutation(string_one='dcw4f', string_two='dcw5f'))

testing_solution_two = SolutionTwo()
print('testing_solution_two-> ',testing_solution_two.checkPermutation(string_one='abcd', string_two='bacd'))
print('testing_solution_two-> ',testing_solution_two.checkPermutation(string_one='3563476', string_two='7334566'))
print('testing_solution_two-> ',testing_solution_two.checkPermutation(string_one='wef34f', string_two='wffe34'))
print('testing_solution_two-> ',testing_solution_two.checkPermutation(string_one='abcd', string_two='d2cba'))
print('testing_solution_two-> ',testing_solution_two.checkPermutation(string_one='2354', string_two='1234'))
print('testing_solution_two-> ',testing_solution_two.checkPermutation(string_one='dcw4f', string_two='dcw5f'))
