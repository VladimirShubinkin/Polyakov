def f(first, s, step):
    if 40 <= first + s <= 49:
        return step % 2 == 0
    if first + s > 49:
        return step % 2 != 0
    if step == 0:
        return False
    calls = [f(first + 1, s, step - 1),
             f(first, s + 1, step - 1),
             f(first * 2, s, step - 1),
             f(first, s * 2, step - 1)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(1, 26):
    if f(14, s, 2):
        print('19)', s)
count = 0
for s in range(1, 26):
    if f(14, s, 3) and not f(14, s, 1):
        count += 1
        print(s)
print('20)', count)
for s in range(1, 26):
    if (f(14, s, 2) or f(14, s, 4)) and not f(14, s, 2):
        print('21)', s)
