a, b, c = map(int, input().split())
def print_rectangle(value):
    print(value)
    print('x'*value)
    print('x'+' '*(value-2)+'x')
    print('x'+' '*(value-2)+'x')
    print('x'*value)

for number in [a, b, c]:
    print_rectangle(number)
