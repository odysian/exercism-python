def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")
    cleaned = question[8:-1]

    if not cleaned:
        raise ValueError("syntax error")

    cleaned = cleaned.replace("divided by", "divided_by")
    cleaned = cleaned.replace("multiplied by", "multiplied_by")
    tokens = cleaned.split()
    operations = ["plus", "minus", "divided_by", "multiplied_by"]

    try:
        result = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")

    i = 1
    while i < len(tokens):
        op = tokens[i]
        if op not in ["plus", "minus", "divided_by", "multiplied_by"]:
            try:
                int(op)
                is_number = True
            except ValueError:
                is_number = False
            if is_number:
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")

        if i + 1 >= len(tokens):
            raise ValueError("syntax error")
        try:
            num = int(tokens[i + 1])
        except ValueError:
            raise ValueError("syntax error")

        if op == "plus":
            result += num
        elif op == "minus":
            result -= num
        elif op == "divided_by":
            result //= num
        elif op == "multiplied_by":
            result *= num

        i += 2
    return result
