'''
+1 +4 *3 >= 88
'''

def f(s, step):
    if s >= 88:
        return step % 2 == 0
    if step == 0:
        return False
    calls = [f(s + 1, step - 1), f(s + 4, step - 1), f(s * 3, step - 1)]
    if (step - 1) % 2 == 0:
        return any(calls)
    return all(calls)


for s in range(1, 88):
    if f(s, 2):
        print('19)', s)
for s in range(1, 88):
    if f(s, 3) and not f(s, 1):
        print('20)', s)
for s in range(1, 88):
    if (f(s, 4) or f(s, 2)) and not f(s, 2):
        print('21)', s)
