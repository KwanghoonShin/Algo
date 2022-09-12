import numpy as np
import random
N, M, K = map(int, input().split())
print(N, '', M, '', K)

array = list(map(int, input().split()))
print(array)

array.sort()
result = 0
count = 0

for _ in range(M):
    if count == K:
        result += array[-2]
        count = 0
    else:
        result += array[-1]
    count += 1

print(result)