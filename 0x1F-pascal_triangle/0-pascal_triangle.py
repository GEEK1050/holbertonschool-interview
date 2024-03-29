#!/usr/bin/python3
"""0-pascal_triangle"""


def factorial(n):
    """factorial:
        return factorial number of n
    """
    _factorial = 1
    for i in range(1, n + 1):
        _factorial = _factorial * i
    return _factorial


def pascal_triangle(n):
    """
    pascal_triangle:
        a function that returns a list of lists of
        integers representing the Pascal’s triangle

        if n <= 0:
            it returns an empty array
    """
    if n <= 0:
        return []

    triangle_p = []
    row = []

    for i in range(n):
        for j in range(i + 1):
            element = factorial(i) // (factorial(j) * factorial(i-j))
            row.append(element)
        triangle_p.append(row)
        row = []
    return triangle_p
