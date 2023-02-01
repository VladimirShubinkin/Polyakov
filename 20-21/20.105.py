def f(a, b, cur_step, stop_step):
    if a + b >= 259:
        return cur_step % 2 == stop_step % 2
    if cur_step == stop_step:
        return False
    if (cur_step + 1) % 2 == stop_step % 2:
        return (f(a + 1, b, cur_step + 1, stop_step)
                or f(a, b + 1, cur_step + 1, stop_step)
                or f(a * 2, b, cur_step + 1, stop_step)
                or f(a, b * 2, cur_step + 1, stop_step))
    return (f(a + 1, b, cur_step + 1, stop_step)
            and f(a, b + 1, cur_step + 1, stop_step)
            and f(a * 2, b, cur_step + 1, stop_step)
            and f(a, b * 2, cur_step + 1, stop_step))


for s in range(1, 242):
    for stop in range(5):
        if f(17, s, 0, stop):
            if stop == 3:
                print(s)
            break

    
