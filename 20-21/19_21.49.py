from math import ceil


def f(first, s, step):
    if first + s <= 20:
        return step % 2 == 0
    if step == 0:
        return False
    calls = [f(first - 1, s, step - 1),
             f(first, s - 1, step - 1),
             f(ceil(first / 2), s, step - 1),
             f(first, ceil(s / 2), step - 1)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(11, 100):
    if f(10, s, 2):
        print('19)', s)
for s in range(11, 100):
    if not f(10, s, 1) and f(10, s, 3):
        print('20)', s)
for s in range(11, 100):
    if f(10, s, 4) and not f(10, s, 2):
        print('21', s)
