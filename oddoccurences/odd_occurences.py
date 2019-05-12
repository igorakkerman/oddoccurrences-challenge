def odd_occurences(a):
    if len(a) % 2 != 1:
        raise ValueError("List must contain an odd number of items.")

    items = set()

    for item in a:
        if item in items:
            items.remove(item)
        else:
            items.add(item)

    if len(items) != 1:
        raise ValueError("List must only contain paired items and a single non-paired item.")

    return items.pop()
