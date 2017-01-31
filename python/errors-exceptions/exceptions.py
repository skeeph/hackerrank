t = int(input())
for _ in range(t):
    try:
        a, b = map(int, input().strip().split(" "))
        print(a // b)
    except ZeroDivisionError as ze:
        print("Error Code: integer division or modulo by zero")
    except ValueError as we:
        print("Error Code:", we)
