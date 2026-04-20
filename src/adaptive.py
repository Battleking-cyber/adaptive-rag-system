def dynamic_k(query):
    length = len(query.split())

    if length < 4:
        return 2
    elif length < 8:
        return 4
    else:
        return 6
