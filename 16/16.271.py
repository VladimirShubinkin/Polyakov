def f(n):
    if n == 247_557:
        return 1
    return (n + 3) * f(n - 3)


print(f(247_563) / 519 - 477 * f(247_560) / f(247_557))
