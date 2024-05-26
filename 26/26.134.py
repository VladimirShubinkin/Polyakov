with open('files/26-134.txt') as f:
    n, T = map(int, f.readline().split())
    queues = {'G': [], 'W': [], 'M': []}
    for line in f.readlines():
        t_in, dt, category = line.split()
        queues[category].append((int(t_in), int(dt)))
for category in queues:
    queues[category].sort()

firsts = {category: min(queues[category]) for category in queues}
first_cat = min(firsts, key=firsts.get)
first = queues[first_cat].pop(0)
counter = {'G': 0, 'W': 0, 'M': 0}
counter[first_cat] += 1
last = first_cat
free = sum(first)
for cur_minute in range(T + 1):
    if cur_minute >= free:
        for category in queues:
            if queues[category] and queues[category][0][0] <= cur_minute:
                counter[category] += 1
                free += queues[category].pop(0)[1]
                last = category
                break
        else:  # если очередь иссякла, увеличиваем время, с которого начнётся приём следующего
            free += 1

print(sum(counter.values()))
print(counter[last])
