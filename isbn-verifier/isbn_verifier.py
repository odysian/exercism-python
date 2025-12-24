def is_valid(isbn):
    s = isbn.replace("-", "")

    # Check length
    if len(s) != 10:
        return False

    # Seperate body and check
    body = s[:-1]
    check = s[-1]

    if not body.isdigit():
        return False

    # Calc check value
    if check == "X":
        check_val = 10
    elif check.isdigit():
        check_val = int(check)
    else:
        return False

    digits = [int(char) for char in body]
    digits.append(check_val)

    mult = 10
    total = 0
    for d in digits:
        total += d * mult
        mult -= 1
    return total % 11 == 0
