def is_palindrome(num):
    num = str(num)
    return num == ''.join(list(reversed(num)))

n=int(input())
x=map(int, input().split(" "))
