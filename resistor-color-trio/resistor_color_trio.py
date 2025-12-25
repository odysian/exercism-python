COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):

    c1 = COLORS.index(colors[0])
    c2 = COLORS.index(colors[1])
    c3 = COLORS.index(colors[2])

    return (c1 * 10 + c2) * (10**c3)


def label(colors):

    num = value(colors)

    units = [(1_000_000_000, "gigaohms"), (1_000_000, "megaohms"), (1_000, "kiloohms")]

    for threshold, suffix in units:
        if num >= threshold and num % threshold == 0:
            return f"{num // threshold} {suffix}"

    return f"{num} ohms"


if __name__ == "__main__":
    print(label(["brown", "green", "black"]))
    print(value(["brown", "green", "violet"]))
