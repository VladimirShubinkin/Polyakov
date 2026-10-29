from math import dist

def get_max_dist(cluster):
    max_dist = 0
    for x1, y1, vx1, vy1, m1, p1, e1 in cluster:
        for x2, y2, vx2, vy2, m2, p2, e2 in cluster:
            if p1 == p2 == 'IV':
                max_dist = max(max_dist, dist((x1, y1), (x2, y2)))
    return max_dist


data = []
with open('27_31908_31908.txt') as f:
    for line in f.readlines():
        x, y, vx, vy, m, p = line.replace(',', '.').split()
        x, y, vx, vy, m = map(float, (x, y, vx, vy, m))
        e = 0.5 * m * (vx * vx + vy * vy)
        data.append((x, y, vx, vy, m, p, e))

clusters = [[], [], [], []]
for x, y, vx, vy, m, p, e in data:
    if e > 12:
        clusters[0].append((x, y, vx, vy, m, p, e))
    elif e > 8:
        clusters[1].append((x, y, vx, vy, m, p, e))
    elif e > 4:
        clusters[2].append((x, y, vx, vy, m, p, e))
    else:
        clusters[3].append((x, y, vx, vy, m, p, e))

q1 = max(get_max_dist(cluster) for cluster in clusters)
centers = [sorted(cluster, key=lambda point: point[-1])[len(cluster) // 2] for cluster in clusters]
q2 = max(center[-1] for center in centers)

print(int(q1 * 10_000), int(q2 * 10_000))
