def is_pangram(sentence):

    # Remove punctuation and set chars to lower
    cleaned = [char.lower() for char in sentence if char.isalpha()]

    # Convert cleaned to set to remove dupes, check length
    return len(set(cleaned)) == 26
