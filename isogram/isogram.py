def is_isogram(string):

    # Clean string to only accept alphanum chars and change to lowercase
    cleaned = [char.lower() for char in string if char.isalpha()]

    # Compare length with set to check for dupes
    return len(cleaned) == len(set(cleaned))
