with open('26data/26-86.txt') as f:
    n = int(f.readline())
    a = sorted([list(map(int, pair.split())) for pair in f.readlines()])
    max_time = a[-1][0]
    # print(max_time)
times = [[] for _ in range(60 * 24)]
dishes = {}
for time, dish in a:
    dishes[dish] = dishes.get(dish, []) + [time]
    times[time].append((-1)**(len(dishes[dish]) % 2 + 1))
# наибольшее кол-во блюд, приготовленных за час
'''
max_count = 0
for i in range(max_time + 1 - 60):
    cur_count = 0
    start = i
    end = i + 60
    for dish, time_list in dishes.items():
        hour = list(filter(lambda x: start <= x <= end, time_list))
        if hour:
            first = hour[0]
            cur_count += len(hour) // 2
            cur_count -= len(hour) % 2 == 0 and time_list.index(first) % 2
    max_count = max(max_count, cur_count)
print(max_count)'''
# наибольшее кол-во блюд, приготовление которых закончилось в текущий час
max_count = 0
for i in range(max_time + 1 - 60):
    hour = times[i:i+60]
    count = 0
    for minute in hour:
        count += minute.count(-1)
    max_count = max(max_count, count)
print(max_count)

# среднее время приготовления блюда
max_aver = 0
max_aver_dish = 0
for dish, time_list in dishes.items():
    s = aver = 0
    for i in range(1, len(time_list), 2):
        s += time_list[i] - time_list[i - 1]
    k = len(time_list) // 2
    if k:
        aver = s / k
    if aver > max_aver:
        max_aver = aver
        max_aver_dish = dish
print(max_aver_dish)