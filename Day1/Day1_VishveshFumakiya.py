#Day 1
def sort(i):
    zeros = i.count(0)

    k = 0 
    while zeros:
        i[k] = 0
        zeros = zeros - 1
        k = k + 1

    for k in range(k, len(i)):
        i[k] = 1

i = [1, 0, 1, 0, 1, 0, 0, 1]
sort(i)

print(i)