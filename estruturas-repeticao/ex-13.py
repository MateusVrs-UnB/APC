array = list()
while True:
    number = int(input())
    if number != -1:
        array.append(number)
    else:
        print(sum(array)//(len(array)))
        break
