n, k = map(int, input().strip().split(" "))
price = list(map(int, input().strip().split(" ")))
billed = int(input().strip())
actual = (sum(price) - price[k])/2
if billed == actual:
    print("Bon Appetit")
else:
    print(int(billed - actual))
