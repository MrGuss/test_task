"""
Задание №1

Не вполне понятно требование к библиотеке по незнанию типа фигуры в compile-time.
Насколько я понимаю это можно сделать в пользовательском коде через получение ввода,
и выбор исполняемого метода в зависимости от ввода.
"""

def calc_circle(r):
    """
    Calculates area of circle with radius r
    :param r: radius of circle
    :return: area of circle
    """
    assert r>0
    return 3.14159265359*r**2

def calc_triang(a,b,c):
    """
    Calculates area of triangle with sides a,b,c

    :param a,b,c: side of triangle
    :return: area of triangle
    """
    assert a>0 and b>0 and c>0
    assert sum(sorted([a,b,c])[0:2])>max(a,b,c)
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
    
def calc_fig(fig, *args):
    """
    Calculates area of given figure

    :param fig: type of figure; "c" for circle, "t" for triangle
    :param args: figure features; radius for circle, sides for triangle
    :return: area of figure
    """
    if fig == "c":
        return calc_circle(*args)
    elif fig =="t":
        return calc_triang(*args)
    else:
        raise ValueError("Unknown figure type: " + str(fig))

def check_triang(a,b,c):
    """
    Checks if triangle is right

    :param a,b,c: sides of triangle
    :return: return True if right, otherwise False
    """
    assert a>0 and b>0 and c>0
    assert sum(sorted([a,b,c])[0:2])>max(a,b,c)
    a, b, c = sorted([a,b,c])
    if (a**2+b**2) == c**2:
        return True
    else:
        return False
