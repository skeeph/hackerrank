def split_and_join(line: str) -> str:
    return "-".join(line.split(" "))


line = input()
result = split_and_join(line)
print(result)
