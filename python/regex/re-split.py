print(*filter(lambda x: len(x)>0, __import__("re").split("[,.]", input())), sep="\n")
