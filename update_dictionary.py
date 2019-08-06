def update_dictionary(d, key, value):
    if key in d:
        val = d.get(key)
        val.append(value)
        d[key] = val
    elif 2 * key in d:
        val = d.get(2 * key)
        val.append(value)
        d[2 * key] = val
    else:
        d[2 * key] = [value]







d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

#принято на Stepik