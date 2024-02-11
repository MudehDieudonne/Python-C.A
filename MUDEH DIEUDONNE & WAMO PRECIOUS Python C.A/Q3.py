import cmath

def quadratic_roots(a, b, c):
    """Compute the roots of the quadratic equation ax^2 + bx + c = 0"""
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    return sol1, sol2

a = 1.2
b = 2.3
c = -3.4

sol1, sol2 = quadratic_roots(a, b, c)
print(f"The roots of the quadratic equation {a}x^2 + {b}x + {c} = 0 are {sol1:.2f} and {sol2:.2f}.")