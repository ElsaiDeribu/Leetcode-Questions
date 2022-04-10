class Solution(object):
    def fizzBuzz(self, n):
        arr = []
        for i in range(n+1):
            if i == 0:
                continue
            if (i % 5) == 0 and (i % 3) == 0:
                arr.append("FizzBuzz")
            elif (i % 3) == 0:
                arr.append("Fizz")
            elif (i % 5) == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr