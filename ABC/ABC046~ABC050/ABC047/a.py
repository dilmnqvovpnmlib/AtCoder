a, b, c = map(int, input().split())

print('Yes' if a + b + c - 2 *  max(a, b, c) == 0 else 'No')