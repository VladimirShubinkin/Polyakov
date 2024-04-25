with open('./26data/26-130.txt') as f:
    n = int(f.readline())
    clients_count = [0]*1441
    for i in range(n):
        t_in, t_out = map(int, f.readline().split())
        clients_count[t_in] += 1
        clients_count[t_out + 1] -= 1

for i in range(1, 1441):
    clients_count[i] += clients_count[i - 1]
max_count = max(clients_count)
max_count_count = 0
for i in range(1, 1441):
    if clients_count[i] == max_count and clients_count[i] > clients_count[i - 1]:
        max_count_count += 1
print(max_count_count, max_count)
