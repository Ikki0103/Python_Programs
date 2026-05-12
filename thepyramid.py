rows = 10


def pyramid_triangle():
    for i in range(1, rows-1):
        spaces = ' ' * (rows-i)  # this pushes the stars middle
        stars = "*" * (2*i-1)  # count of star per row
        print(spaces+stars)


def pyramid_inverted():
    for i in range(rows, 0, -1):  # ends at 0, the -1 is indication of reverse starts as the bottom
        spaces = ' ' * (rows-i)  # this pushes the stars middle
        stars = '*' * (2*i-1)  # count of star per row
        print(spaces+stars)


pyramid_triangle()
pyramid_inverted()
