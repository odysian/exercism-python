PATTERNS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}

# [" _ ", "| |", "|_|", "   "]


def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    rows = []
    for row_start in range(0, len(input_grid), 4):
        lines = input_grid[row_start : row_start + 4]

        digits = []
        num_digits = len(lines[0]) // 3

        for digit_idx in range(num_digits):
            start = digit_idx * 3
            end = start + 3

            pattern = (
                lines[0][start:end],
                lines[1][start:end],
                lines[2][start:end],
                lines[3][start:end],
            )

            digit = PATTERNS.get(pattern, "?")
            digits.append(digit)

        rows.append("".join(digits))

    return ",".join(rows)
