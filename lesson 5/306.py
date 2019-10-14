def min(a, b, c, d):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    if d < min:
        min = d
    return min

n = list(map(int, input().split()))

print(min(n[0], n[1], n[2], n[3]))