N = int(input())
problems = 0
for n in range(N):
    if sum(map(int, input().split())) >= 2:
        problems += 1
print(problems)