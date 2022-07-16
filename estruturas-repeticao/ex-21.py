N = int(input())
for number in range(1, N+1):
    if not number % 15:
        print('Fizz Buzz')
    elif not number % 3:
        print('Fizz')
    elif not number % 5:
        print('Buzz')
    else:
        print(number)