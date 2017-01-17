def reduce(s: str) -> str:
    s += "/"
    res = ""
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            i += 2
            continue
        else:
            res += s[i]
        i += 1
    if res != s[:-1]:
        res = reduce(res)
    return res


red = reduce(input().strip())
if len(red) > 0:
    print(red)
else:
    print("Empty String")
