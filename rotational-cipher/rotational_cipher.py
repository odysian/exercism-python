def rotate(text, key):
    res = ""

    for c in text:
        # If char is not a letter
        if not c.isalpha():
            res += c
            continue

        # Calculate base value of both lower and uppercase
        base = ord("a") if c.islower() else ord("A")

        # Set index for alphabet
        index_0_to_25 = ord(c) - base
        # If index goes over 25, modulo it back to 0-25
        new_index = (index_0_to_25 + key) % 26
        # Convert ord back to character by adding base
        new_char = chr(new_index + base)
        res += new_char

    return res
