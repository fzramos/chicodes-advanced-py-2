"""
Write a function to print all numbers from 1 to n, but there are some constraints.
If the number is divisible by 3, write Fizz instead of the number
If the number is divisible by 5, write Buzz instead of the number
If the number is divisible by 3 and 5 both, write FizzBuzz instead of the number
Otherwise, simply write the number
Input: n == 10
Input: n == 20
"""

def fizzbuzz(n):  
    for i in range(1, n+1):
        printed = False
        if i % 3 == 0:
            print('Fizz', end='')
            printed = True
        if i % 5 == 0:
            print('Buzz', end='')
            printed = True
        if not printed:
            print(i)
        else:
            print('\n', end='')

### Attemps to find more efficient answers
def fizzbuzz3(n):
    for i in range(1, n+1):
        div3 = (i % 3 == 0)
        div5 = (i % 5 == 0)
        if div3 or div5:
            if div3:
                print('Fizz', end='')
            if div5:
                print('Buzz', end='')
            print()
        else:
            print(i)

#doesn't work Fizz printw with the number that is makes it fizz
def fizzbuzz3(n):  
    for i in range(1, n+1):
        if i % 3 == 0:
            print('Fizz', end='')
        if i % 5 == 0:
            print('Buzz', end='')
        else:
            print(i, end='')
        print('')




if __name__ == '__main__':
    fizzbuzz(20)
    # print('')
    # fizzbuzz(1000)

    
