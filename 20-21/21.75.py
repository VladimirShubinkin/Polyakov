'''75)	Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может
а) добавить в любую кучу один камень;
б) увеличить количество камней в куче в три раза.
Игра завершается в тот момент, когда суммарное количество камней в двух кучах становится не менее 70, побеждает игрок,
сделавший последний ход. В начальный момент в первой куче было 6 камней, а во второй – S камней, 1 ≤ S ≤ 63.
'''

def f(a, s, cur_step, stop_step):
    if a + s >= 70:
        return cur_step % 2 == stop_step % 2
    if cur_step == stop_step:
        return False
    if (cur_step + 1) % 2 == stop_step % 2:
        return (f(a + 1, s, cur_step + 1, stop_step)
                or f(a, s + 1, cur_step + 1, stop_step)
                or f(a * 3, s, cur_step + 1, stop_step)
                or f(a, s * 3, cur_step + 1, stop_step))
    return (f(a + 1, s, cur_step + 1, stop_step)
            and f(a, s + 1, cur_step + 1, stop_step)
            and f(a * 3, s, cur_step + 1, stop_step)
            and f(a, s * 3, cur_step + 1, stop_step))


c = 0
for s in range(1, 64):
    for stop in range(1, 5):
        if f(6, s, 0, stop):
            if stop == 4:
                print(s)
                c = s
            # break
print('Ответ:', c)