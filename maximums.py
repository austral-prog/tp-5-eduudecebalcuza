def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x or y


def max_of_three (x, y, z):
    if (x > y and x > z):
        return x
    elif (y > x and y > z):
        return y
    elif (z > y and z > x):
        return z
    else:
        return x or y or z
