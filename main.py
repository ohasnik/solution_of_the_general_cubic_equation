#!/usr/bin/python3

from sympy import symbols, Eq, solve

print("Solution of the general cubic equation ax^(3) + bx^(2) + cx + d = 0")
print("(c) 2024 Ondřej Hasník - ondhas SOFTWARE - All rights reserved")
print("This program is published under the MIT license: https://mit-license.org/")
print("The source code is available at: https://github.com/ondhas/solution_of_the_general_cubic_equation")
print("Please report errors to ondhas@skiff.com")


def solve_cubic_equation():
    x, a, b, c, d = symbols('x a b c d')
    a_value = float(input("Enter the value of a: "))
    b_value = float(input("Enter the value of b: "))
    c_value = float(input("Enter the value of c: "))
    d_value = float(input("Enter the value of d: "))
    equation = Eq(a * x ** 3 + b * x ** 2 + c * x + d, 0)
    equation_substituted = equation.subs({a: a_value, b: b_value, c: c_value, d: d_value})
    solutions = solve(equation_substituted, x)
    print("Solutions:")
    for solution in solutions:
        print(solution.evalf())


if __name__ == "__main__":
    solve_cubic_equation()
