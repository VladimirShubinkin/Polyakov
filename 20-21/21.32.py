def f(a, s, cur_step, stop_step):
    if a + s >= 40:
        return cur_step % 2 == stop_step % 2
    if cur_step == stop_step:
        return False
    calls = [f(a + 1, s, cur_step + 1, stop_step),
             f(a, s + 1, cur_step + 1, stop_step),
             f(a * 2, s, cur_step + 1, stop_step),
             f(a, s * 2, cur_step + 1, stop_step)]
    if (cur_step + 1) % 2 == stop_step % 2:
        return any(calls)
    return all(calls)


count = 0
for s in range(1, 31):
    for stop in range(1, 5):
        if f(9, s, 0, stop):
            if stop == 4:
                count += 1
            break
print(count)
