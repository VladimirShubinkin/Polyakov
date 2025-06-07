def f(a, b, s, cur_step, win_steps):
    if a + b + s >= 71:
        return cur_step in win_steps
    if cur_step > max(win_steps):
        return False
    calls = [f(a + 3, b, s, cur_step + 1, win_steps),
             f(a * 2, b, s, cur_step + 1, win_steps),
             f(a, b + 3, s, cur_step + 1, win_steps),
             f(a, b * 2, s, cur_step + 1, win_steps),
             f(a, b, s + 3, cur_step + 1, win_steps),
             f(a, b, s * 2, cur_step + 1, win_steps)]
    if (cur_step + 1) % 2 == win_steps[0] % 2:
        return any(calls)
    return all(calls)


ans20 = []
ans21 = 0
for s in range(1, 59):
    if f(7, 5, s, 0, [3]):
        ans20.append(s)
    if f(7, 5, s, 0, [2, 4]) and not f(7, 5, s, 0, [2]):
        ans21 = s
print('Задание 20: ', min(ans20), max(ans20))
print('Задание 21: ', ans21)
