def triangular_pattern(limit):
    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")

        print("")


triangular_pattern(5)


def reverse_triangle_pattern(limit):
    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            if j <= limit + 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


reverse_triangle_pattern(10)
