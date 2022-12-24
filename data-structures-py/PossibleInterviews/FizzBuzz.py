#  Print integers one-to-N, 
# but print “Fizz” if an integer is divisible by three, 
# “Buzz” if an integer is divisible by five, 
# and “FizzBuzz” if an integer is divisible by both three and five.

class Solution:
  def FizzBuzz(self, fbnum: int) -> str:

    if fbnum == 0:
      print(0)

    for i in range(1,fbnum):
      # Starting from highest to lowest
      # 15 is divisible by 3 and 5 so use that
      if (i % 15 == 0):
        print('FizzBuzz')
        continue
      elif i % 5 == 0:
        print('Buzz')
        continue
      elif i % 3 == 0:
        print('Fizz')
        continue
      else:
        print(i)


TestingSolution = Solution()
print('FizzBuzz 100:',TestingSolution.FizzBuzz(100))
