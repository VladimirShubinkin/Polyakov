def f(first, s, step):
    if first >= 78 or s >= 78:
        return step % 2 == 0
    if step == 0:
        return False
    calls = []
    first, s = max(first, s), min(first, s)
    if first != s:
        calls.append(f(first, s * 2, step - 1))
    for i in range(1, 4):
        calls.append(f(first + i, s, step - 1))
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)

min_s = 1000
for s in range(1, 78):
    for first in range(1, 78):
        if f(first, s, 1):
            min_s = min(min_s, first + s)
print('19)', min_s)

for s in range(1, 78):
    if not f(25, s, 1) and f(25, s, 3):
        print('20)', s)

for s in range(1, 78):
    if f(69, s, 4) and not f(69, s, 2):
        print('21)', s)
