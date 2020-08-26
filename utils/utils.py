def decimal_to_binary(n, bits=None):
    out = [int(_) for _ in bin(n).replace("0b", "")]
    if bits is not None:
        out = [_ for _ in range(bits - len(out))] + out
    return out


