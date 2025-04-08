from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        name, type_ = input().split()
        clothes[type_] += 1

    result = 1
    for count in clothes.values():
        result *= (count + 1)
    print(result - 1)