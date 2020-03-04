import sympy as sy

x1, x2 = sy.symbols("x1 x2")

equations = [
    sy.Eq( 2*x1 + 1*x2 ,  10 ),
    sy.Eq( 1*x1 - 2*x2 ,  11 )
]

print(sy.solve(equations))