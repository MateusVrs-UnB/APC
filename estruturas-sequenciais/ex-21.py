a, b, c = map(int, input().split())
def print_rectangle(value):
    print(value)
    print('+'*value)
    print('+'+' '*(value-2)+'+')
    print('+'*value)

for number in [a, b, c]:
    print_rectangle(number)
