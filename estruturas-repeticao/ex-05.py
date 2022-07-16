array = list(map(int, input().split()))
final, changes = 1, 0
while final < len(array):
    if array[final-1] > array[final]:
        array[final-1], array[final] = array[final], array[final-1]
        changes += 1
        if final > 1:
            final -= 1
    else:
        final += 1
print(changes)
