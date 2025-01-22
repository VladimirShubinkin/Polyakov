from math import dist


def get_clusters_A(filename):
    c1 = []
    c2 = []
    with open(filename) as f:
        for line in f.readlines():
            x, y = map(float, line.replace(',', '.').split())
            if x < 8 and y < 2:
                c1.append((x, y))
            else:
                c2.append((x, y))
    return c1, c2


def get_clusters_B(filename):
    c1 = []
    c2 = []
    c3 = []
    with open(filename) as f:
        for line in f.readlines():
            x, y = map(float, line.replace(',', '.').split())
            if 5 < x < 8 and -2/3 * x + 16/3 < y < 6:
                c1.append((x, y))
            elif x < 7:
                c2.append((x, y))
            else:
                c3.append((x, y))
    return c1, c2, c3


def get_centr_coords(cluster: list[tuple[float, float]]) -> tuple[float, float]:
    min_sum = float('inf')
    x0 = y0 = None
    for p0 in cluster:
        cur_sum = 0
        for p in cluster:
            cur_sum += dist(p0, p)
        if cur_sum < min_sum:
            min_sum = cur_sum
            x0, y0 = p0
    return x0, y0


def solve_A():
    (x1, y1), (x2, y2) = map(get_centr_coords, get_clusters_A('files/27-57a.txt'))
    px = (x1 + x2) / 2
    py = (y1 + y2) / 2
    print(int(px * 100_000), int(py * 100_000))


solve_A()


def solve_B():
    (x1, y1), (x2, y2), (x3, y3) = map(get_centr_coords, get_clusters_B('files/27-57b.txt'))
    px = (x1 + x2 + x3) / 3
    py = (y1 + y2 + y3) / 3
    print(int(px * 100_000), int(py * 100_000))


solve_B()