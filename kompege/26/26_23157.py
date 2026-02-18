with open('26vit2 (1)_23157.txt') as f:
    boxes_0 = []
    boxes_1 = []
    for line in f.readlines():
        size, m = map(int, line.split())
        if m == 0:
            boxes_0.append(size)
        else:
            boxes_1.append(size)
boxes_0.sort(reverse=True)
boxes_1.sort(reverse=True)
max_count = 0
cur_box = boxes_0[0]
count = 1
last = 0
i0 = i1 = 0
while i0 < len(boxes_0) and i1 < len(boxes_1):
    while i1 < len(boxes_1) and cur_box - boxes_1[i1] < 7:
        i1 += 1
    if i1 < len(boxes_1):
        count += 1
        cur_box = boxes_1[i1]
        if count > max_count:
            max_count = count
            last = cur_box
    else:
        break
    while i0 < len(boxes_0) and cur_box - boxes_0[i0] < 7:
        i0 += 1
    if i0 < len(boxes_0):
        count += 1
        cur_box = boxes_0[i0]
        if count > max_count:
            max_count = count
            last = cur_box
cur_box = boxes_1[0]
count = 1
i0 = i1 = 0
while i0 < len(boxes_0) and i1 < len(boxes_1):
    while i0 < len(boxes_0) and cur_box - boxes_0[i0] < 7:
        i0 += 1
    if i0 < len(boxes_0):
        count += 1
        cur_box = boxes_0[i0]
        if count > max_count:
            max_count = count
            last = cur_box
    else:
        break
    while i1 < len(boxes_1) and cur_box - boxes_1[i1] < 7:
        i1 += 1
    if i1 < len(boxes_1):
        count += 1
        cur_box = boxes_1[i1]
        if count > max_count:
            max_count = count
            last = cur_box
print(max_count, last)
