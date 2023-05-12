with open('files/27-59b.txt') as f:
    n, *a = map(int, f.readlines())
counter = [0]*10
for x in a:
    temp_counter = counter[:]
    for d in range(10):
        temp_counter[(d + x) % 10] += counter[d]
    temp_counter[x % 10] += 1
    counter = temp_counter[:]
print(counter[5])
