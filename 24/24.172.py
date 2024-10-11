with open('24data/24-171.txt') as f:
    lines = f.read().splitlines()
xyz = 'XYZ'
j = 0
max_len = 0
for line in lines:
    cur_len = 0
    for i in range(len(line)):
        if line[i] == xyz[j]:
            cur_len += 1
            j = (j + 1) % 3
        elif line[i] in xyz:
            cur_len = 1
            j = (xyz.find(line[i]) + 1) % 3
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)
