n = int(input())
for i in range(n * 2):
    if i < n:
        print(" " * (2 * n + 2 * n - i - 1) + "/" + " " * (2 * i) + "\\")
    elif i == 2 * n - 1:
        print(
            " " * (2 * n - 1 - i)
            + "/"
            + "_" * (i - n) * 2
            + "\\"
            + " " * (2 * n - 1 - i) * 2
            + "/"
            + "_" * (2 * i)
            + "\\"
            + " " * (2 * n - 1 - i) * 2
            + "/"
            + "_" * (i - n) * 2
            + "\\"
        )
    else:
        print(
            " " * (2 * n - 1 - i)
            + "/"
            + " " * (i - n) * 2
            + "\\"
            + " " * (2 * n - 1 - i) * 2
            + "/"
            + " " * (2 * i)
            + "\\"
            + " " * (2 * n - 1 - i) * 2
            + "/"
            + " " * (i - n) * 2
            + "\\"
        )