def digital_root(n: int, base: int = 10) -> int:
   
    def recursive_sum_of_digits(n: int, base=10) -> int:
        if n // base == 0:
            return n
        else:
            return n % base + recursive_sum_of_digits(n // base, base)

    value: int = recursive_sum_of_digits(n, base=base)
    if value // base == 0:
        return value
    else:
        return digital_root(value)


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
