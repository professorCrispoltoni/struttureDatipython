n = int(input())
quote = list(map(int, input().split()))
picchi = 0
for i in range(1, n - 1):
    if quote[i] > quote[i - 1] and quote[i] > quote[i + 1]:
        picchi += 1
print(picchi)