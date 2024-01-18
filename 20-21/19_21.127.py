def f(s, step):
    if s >= 111:
        return step % 2 == 0
    if step == 0:
        return False
    calls = [f(s + 1, step - 1), f(s + 3, step - 1), f(s * 4, step - 1)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(1, 111):
    if f(s, 2):
        print(f'19) {s}')
for s in range(1, 111):
    if f(s, 3) and not f(s, 1):
        print(f'20) {s}')
for s in range(1, 111):
    if (f(s, 4) or f(s, 2)) and not f(s, 2):
        print(f'21) {s}')
