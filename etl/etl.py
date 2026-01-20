def transform(legacy_data):
    res = {}
    for point, letters in legacy_data.items():
        for letter in letters:
            res[letter.lower()] = point
    return res

    # return {letter.lower(): point for point, letters in legacy_data.items() for letter in letters}
