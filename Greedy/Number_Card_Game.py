N,M = map(int, input().split())

array = list()
result = 0

for _ in range(N):
    array.append(list(map(int, input().split())))

# choose Raw
min_raw = 0
min_raw = min(array[0])
ch_raw = 0

for i in range(N):
    if min_raw <= min(array[i]):
        min_raw = min(array[i])
        ch_raw = i + 1

# choose maximum value
result = min(array[ch_raw - 1])
print(result)

#what?
