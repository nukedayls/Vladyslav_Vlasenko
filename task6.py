def nextBigger(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x > t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

print(nextBigger(12))
print(nextBigger(513))
print(nextBigger(2017))