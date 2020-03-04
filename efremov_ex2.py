from sympy import *
x, y, z, a, b, c, vx, vy, vz, lmbd, m, g, L, E = symbols('x y z a b c vx vy vz lmbd m g L E')

eqs = [
       Eq(2 * x * vx / a**2 + 2 * y * vy / b**2 + 2 * z * vz / c**2, 0),
       Eq(m * vx * x + m * vy * y + m * vz * z, L),
       Eq(m * (vx**2 + vy**2 + vz ** 2) / 2 + m * g * y, E),
       Eq(lmbd * 4 * x**2 / m / a**4 + 2 * x * vx**2 / a**2 + 2 * y (lmbd * 2 * y / m / b**2 - g) / b**2 + 2 * y * vy**2 / b**2 + lmbd * 4 * z**2 / m / c**4 + 2 * x * vz**2 / c**2, 0)
       ]
print(solve(eqs))