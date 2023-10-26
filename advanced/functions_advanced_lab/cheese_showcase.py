def sorting_cheeses(**kwargs):
    result = ""
    for kind, quantity in sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f"{kind}\n" + "\n".join([str(num) for num in sorted(quantity, key=lambda x: -x)]) + "\n"
    return result
