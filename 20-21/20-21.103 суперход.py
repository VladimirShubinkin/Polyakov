def f(s, step, super):
    if s >= 20:
        return step % 2 == 0
    if step == 0:
        return False
    if super:
        calls = [f(s + 2, step - 1, super), f(s * 2, step - 1, super), f(s, step - 1, super - 1)]
    else:
        calls = [f(s + 2, step - 1, super), f(s * 2, step - 1, super)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(1, 20):
    if f(s, 3, 1) and not f(s, 1, 1):
        print('20)', s)
for s in range(1, 20):
    if any(f(s, steps, 1) for steps in range(2, 20, 2)):
        print('21)', s)
