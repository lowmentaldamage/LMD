import sys


total = 0.0
n = int(sys.stdin.readline().strip())  # number of periods of constant quality of life during the person’s lifetime

for _ in range(n):
    q , y = map(float, sys.stdin.readline().strip().split())
    total += q * y
print(total)
