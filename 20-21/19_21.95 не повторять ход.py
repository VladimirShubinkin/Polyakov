# +1    +2   *2
# >= 43


def f(s, step, k=0):
    if s >= 43:
        return step % 2 == 0
    if step == 0:
        return False
    match k:
        case 0:
            calls = [f(s + 1, step - 1, 1), f(s + 2, step - 1, 2), f(s * 2, step - 1, 3)]
        case 1:
            calls = [f(s + 2, step - 1, 2), f(s * 2, step - 1, 3)]
        case 2:
            calls = [f(s + 1, step - 1, 1), f(s * 2, step - 1, 3)]
        case 3:
            calls = [f(s + 1, step - 1, 1), f(s + 2, step - 1, 2)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(1, 43):
    if f(s, 2):
        print('19)', s)
list_s = []
for s in range(1, 43):
    if f(s, 3) and not f(s, 1):
        list_s.append(s)
print('20)', min(list_s), max(list_s))
for s in range(1, 43):
    if f(s, 4) and not f(s, 2):
        print('21)', s)
