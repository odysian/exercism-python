def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    value = 0
    for position, digit in enumerate(digits[::-1]):
        value += digit * (input_base**position)

    if value == 0:
        return [0]

    output = []
    while value > 0:
        digit = value % output_base
        output.append(digit)

        value = value // output_base

    return output[::-1]
