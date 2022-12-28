





class Solution:
  def PalindromePermutation(self, string: str) -> bool:

    hashmap = {}
    count_odd = 0

    for char in string:
      hashmap[char] = 1 + hashmap.get(char, 0)

      if hashmap[char] % 2 > 0:
        count_odd += 1


testing_solution = Solution()
print('test case 1',testing_solution.PalindromePermutation('Tact Coa'))
print('test case 2',testing_solution.PalindromePermutation('jhsabckuj ahjsbckj'))
print('test case 3',testing_solution.PalindromePermutation('Able was I ere I saw Elba'))
print('test case 4',testing_solution.PalindromePermutation('So patient a nurse to nurse a patient so'))
print('test case 5',testing_solution.PalindromePermutation('Random Words'))
print('test case 6',testing_solution.PalindromePermutation('Not a Palindrome'))
print('test case 7',testing_solution.PalindromePermutation('no x in nixon'))
print('test case 8',testing_solution.PalindromePermutation('azAZ'))

