with open('../26data/26-150.txt') as f:
    n, m, k = map(int, f.readline().split())
    place_row = {i: m + 1 for i in range(1, k + 1)}
    for line in f.readlines():
        row, place = map(int, line.split())
        place_row[place] = min(place_row[place], row)
print(place_row)
max_row = 0
max_place = 0
for i in range(1, k):
    cur_row = min(place_row[i], place_row[i + 1]) - 1
    if cur_row >= max_row:
        max_row = cur_row
        max_place = i + 1
print(max_row, max_place)
