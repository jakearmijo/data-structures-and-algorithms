# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters
# and that you are given the 'true' length of the string
# EXAMPLE 
# INPUT: 'Mr John Smith', 13
# OUTPUT: 'Mr%20John%20Smith

class Solution:
  def URLify(self,string: str) -> str:
    new_string = string.replace(' ', '%20')

    return new_string



testing_solution = Solution()
print('test case 1',testing_solution.URLify('much ado about nothing'))
print('test case 2',testing_solution.URLify('Mr John Smith'))


class SolutionTwo:
  def URLify(self,string: str) -> str:

    new_string = ''
    
    for char in string:
      
      if char == ' ':
        char = '%20'
        new_string += char
      else:
        new_string += char

    return new_string


testing_solution = Solution()
print('test case 1',testing_solution.URLify('much ado about nothing'))
print('test case 2',testing_solution.URLify('Mr John Smith'))

testing_solution_two = SolutionTwo()
print('test case 1',testing_solution_two.URLify('much ado about nothing'))
print('test case 2',testing_solution_two.URLify('Mr John Smith'))


