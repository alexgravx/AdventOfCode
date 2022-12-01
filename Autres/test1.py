with open('/Users/alexandregravereaux/Desktop/text_test1', 'r') as file:
    L = file.read().splitlines()
    L = [int(i) for i in L]

n = 0

for i in range(1, len(L)):
    if L[i] > L[i-1]:
        n += 1

print(n)
