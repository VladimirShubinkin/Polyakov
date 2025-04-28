from math import dist


def get_data(filename):
    coords = []
    with open(filename) as f:
        f.readline()
        for line in f.readlines():
            p = map(float, line.replace(',', '.').split())
            coords.append(p)
    return coords


def get_clusters_B(coords):
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    for x, y in coords:
        if y < -abs(x - 4) + 4:
            cluster_1.append((x, y))
        elif x < 4:
            cluster_2.append((x, y))
        else:
            cluster_3.append((x, y))
    return cluster_1, cluster_2, cluster_3


def get_center(cluster):
    min_sum = float('inf')
    for p0 in cluster:
        cur_sum = sum(dist(p0, p1) for p1 in cluster)
        if cur_sum < min_sum:
            min_sum = cur_sum
            p = p0
    return p


def solve_B():
    coords = get_data('27_B_17834.txt')
    (x1, y1), (x2, y2), (x3, y3) = map(get_center, get_clusters_B(coords))
    px = (x1 + x2 + x3) / 3
    py = (y1 + y2 + y3) / 3
    print(int(px * 100), int(py * 100))


solve_B()
