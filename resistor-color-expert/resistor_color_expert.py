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

TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def value(colors):

    if len(colors) == 1:
        return 0

    c1 = COLORS.index(colors[0])
    c2 = COLORS.index(colors[1])
    zeroes = COLORS.index(colors[-2])

    if len(colors) == 5:
        c3 = COLORS.index(colors[2])
        return (c1 * 100 + c2 * 10 + c3) * (10**zeroes)

    return (c1 * 10 + c2) * (10**zeroes)


def resistor_label(colors):

    num = value(colors)
    if num == 0:
        return "0 ohms"

    tolerance = TOLERANCE[colors[-1]]

    units = [(1_000_000_000, "gigaohms"), (1_000_000, "megaohms"), (1_000, "kiloohms")]

    for threshold, suffix in units:
        if num >= threshold:
            clean_num = f"{num / threshold:g}"
            return f"{clean_num} {suffix} ±{tolerance}%"

    return f"{num} ohms ±{tolerance}%"


if __name__ == "__main__":
    print("running file")
    colors = ["orange", "orange", "black", "red"]

    resistor_label(colors)
