N = int(input())

def findOne(number):
    print(N)
    while number != 1:
        if not number % 2:
            number = number//2
            print(number)
        else:
            number = 3*number + 1
            print(number)

findOne(N)
