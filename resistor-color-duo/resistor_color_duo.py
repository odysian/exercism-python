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

    c1_code = COLORS.index(colors[0])
    c2_code = COLORS.index(colors[1])

    return int(f"{c1_code}{c2_code}")
