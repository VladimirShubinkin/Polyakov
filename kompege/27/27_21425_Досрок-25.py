from math import dist


def get_data(filename):
    coords = []
    with open(filename) as f:
        for line in f.readlines():
            p = map(float, line.replace(',', '.').split())
            coords.append(p)
    return coords


def get_clusters_A(coords):
    cluster_1 = []
    cluster_2 = []
    for x, y in coords:
        if y < 0:
            cluster_1.append((x, y))
        else:
            cluster_2.append((x, y))
    return cluster_1, cluster_2


def get_clusters_B(coords):
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    for x, y in coords:
        if y > 10:
            cluster_1.append((x, y))
        elif x < 10:
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


def solve_A():
    coords = get_data('27_A_21425.txt')
    (x1, y1), (x2, y2) = map(get_center, get_clusters_A(coords))
    px = (x1 + x2) / 2
    py = (y1 + y2) / 2
    print(int(px * 10_000), int(py * 10_000))


def solve_B():
    coords = get_data('27_B_21425.txt')
    (x1, y1), (x2, y2), (x3, y3) = map(get_center, get_clusters_B(coords))
    px = (x1 + x2 + x3) / 3
    py = (y1 + y2 + y3) / 3
    print(int(px * 10_000), int(py * 10_000))


solve_A()
solve_B()
