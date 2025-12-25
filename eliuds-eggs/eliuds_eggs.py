def egg_count(display_value):

    base = 2
    output = []
    while display_value > 0:
        digit = display_value % base
        output.append(digit)

        display_value = display_value // base

    print(output[::-1])
    print(output.count(1))

    return output.count(1)


if __name__ == "__main__":

    egg_count(16)
