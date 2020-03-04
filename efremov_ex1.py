from sympy import *

f = Function('f')
x = Function('x')
y = Function('y')
z = Function('z')

t = Symbol('t')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

f = x(t)**2 / a**2 + y(t)**2 / b**2 + z(t)**2 / c**2 - 1

print(diff(f, x(t)))
print(diff(f, y(t)))
print(diff(f, z(t)))
print()
print('Первая производная: ', diff(f, t))
print()

print('Вторая производная: ', diff(diff(f, t), t))

x, y, z, a, b, c, vx, vy, vz, lmbd, m, g = symbols('x y z a b c vx vy vz lmbd m g')


eq1= (2 * x * vx / a**2 + 2 * y * vy / b**2 + 2 * z * vz / c**2)
eq2= (m * vx * x + m * vy * y + m * vz * z)
eq3= (m * (vx**2 + vy**2 + vz ** 2) / 2 + m * g * y)
eq4= (lmbd * 4 * x**2 / m / a**4 + 2 * x * vx**2 / a**2 + 2 * y (lmbd * 2 * y / m / b**2 - g) / b**2 + 2 * y * vy**2 / b**2 + lmbd * 4 * z**2 / m / c**4 + 2 * x * vz**2 / c**2)
eqs = [
       Eq(2 * x * vx / a**2 + 2 * y * vy / b**2 + 2 * z * vz / c**2, 0),
       Eq(m * vx * x + m * vy * y + m * vz * z, L),
       Eq(m * (vx**2 + vy**2 + vz ** 2) / 2 + m * g * y, E),
       Eq(lmbd * 4 * x**2 / m / a**4 + 2 * x * vx**2 / a**2 + 2 * y (lmbd * 2 * y / m / b**2 - g) / b**2 + 2 * y * vy**2 / b**2 + lmbd * 4 * z**2 / m / c**4 + 2 * x * vz**2 / c**2, 0)
       ]
print(solve(eqs))