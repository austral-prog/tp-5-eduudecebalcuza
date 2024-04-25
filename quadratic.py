# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminant = (math.pow(b, 2) - 4 * a * c)
    if (discriminant > 0):
        x1 = ((-b) + math.sqrt(discriminant)) / 2 * a
        x2 = ((-b) - math.sqrt(discriminant)) / 2 * a
        return (f"({x1}, {x2})")
    
    elif (discriminant == 0):
        x1 = ((-b) + math.sqrt(discriminant)) / 2 * a
        x2 = ((-b) - math.sqrt(discriminant)) / 2 * a
        return (f"({x1 or x2})")
    else:
        return (f"( )")
        
def value_y(a, b, c, x):
    y = (a * math.pow(x, 2) + b * x + c)
    return y


def to_string(a, b, c):
        if (a == 0) and (b != 0) and (c == 0):
        return (f"f(x) = {b} * X")
    elif (a != 0) and (b == 0) and (c != 0):
        return (f"f(x) = {a} * X^2 + {c}")
    elif (a == 0) and (b == 0) and (c != 0):
        return (f"f(x) = {c}")    
    elif (a != 0) and (b != 0) and (c != 0):
        return (f"f(x) = {a} * X^2 + {b} * X + {c}")
    elif (a == 0) and (b != 0) and (c != 0):
        return (f"f(x) = {b} * X + {c}")
    elif (a != 0) and (b == 0) and (c != 0):
        return (f"f(x) = {a} * X^2 + {c}")
    elif (a != 0) and (b != 0) and (c == 0):
        return (f"f(x) = {a} * X^2 + {b} * X")
    elif (a != 0) and (b == 0) and (c == 0):
        return (f"f(x) = {a} * X^2")
    else:
        return (f"f(x) = {0}")


def derivation(a, b, c):
    if (a < 0) and (b):
        return (f"f'(x) = {coeficent} * X + {b}")
    if (a < 0) and (b == 0):
        return (f"f'(x) = {coeficent} * X")
    elif (a > 0) and (b):
        return (f"f'(x) = {coeficent} * X + {b}")
    elif (a > 0) and (b == 0):
        return (f"f'(x) = {coeficent} * X")
    elif (a == 0) and (b):
        return (f"f'(x) = {b}")
    else:
        return (f"f'(x) = {0}")
