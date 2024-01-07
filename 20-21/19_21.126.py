'''
№19
2: П В
   1 0
№20
3: П В П
   2 1 0
№21
4: П В П В
   3 2 1 0
'''
def f(s, step):
    if s >= 59:
        return step % 2 == 0
    if step == 0:
        return False
    calls = [f(s + 1, step - 1), f(s + 3, step - 1), f(s * 4, step - 1)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(1, 59):
    if f(s, 2):
        print('19)', s)
for s in range(1, 59):
    if f(s, 3) and not f(s, 1):
        print('20)', s)
for s in range(1, 59):
    if (f(s, 4) or f(s, 2)) and not f(s, 2):
        print('21)', s)
