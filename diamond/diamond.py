# Outer padding: n - i
# Inner padding: 2 * i - 1


def rows(letter):
    # Get ascii value for letter
    n = ord(letter) - ord("A")
    res = []
    # Build half of the diamond
    for i in range(n + 1):
        char = chr(ord("A") + i)
        outer_padding = " " * (n - i)
        # Build first row without inner padding
        if i == 0:
            row = outer_padding + "A" + outer_padding

        else:
            inner_padding = " " * (2 * i - 1)
            row = outer_padding + char + inner_padding + char + outer_padding
        res.append(row)

    bottom_half = res[:-1][::-1]
    return res + bottom_half
