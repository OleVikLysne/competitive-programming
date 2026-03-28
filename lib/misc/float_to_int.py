def float_to_int(string: str, decimal_shift: int):
    if "." not in string:
        return int(string) * 10**decimal_shift
    l, _, r = string.partition(".")
    decimal_shift -= len(r)
    return int(l+r) * 10**decimal_shift