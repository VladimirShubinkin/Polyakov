# https://education.yandex.ru/ege/task/4e43bee7-572c-4e2e-8805-22fd8a9b50c2

with open('Комбайнер.txt') as f:
    s, w, n, k = map(int, f.readline().split())
    x = [0]*(s + 1)
    for _ in range(n):
        xi = int(f.readline())
        for i in range(max(0, xi - w // 2), min(s, xi + w // 2)):
            x[i] = 1
    length_x = sum(x)
    print(length_x)
    y = [0]*(s + 1)
    for _ in range(k):
        yi = int(f.readline())
        for i in range(max(0, yi - w // 2), min(s, yi + w // 2)):
            y[i] = 1
    length_y = sum(y)
    x_area = length_x * s
    y_area = length_y * (s - length_x)
    print(x_area + y_area)
