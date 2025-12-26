def translate_atbash(text):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    return text.translate(table)


def encode(plain_text):

    text = plain_text.lower()
    cleaned = "".join(c for c in text if c.isalnum())
    translated_text = translate_atbash(cleaned)

    chunks = []
    for i in range(0, len(translated_text), 5):
        chunks.append(translated_text[i : i + 5])

    return " ".join(chunks)


def decode(ciphered_text):

    cleaned = ciphered_text.replace(" ", "")

    return translate_atbash(cleaned)
