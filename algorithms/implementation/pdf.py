from string import ascii_lowercase

h = [int(h_temp) for h_temp in input().strip().split(' ')]
H = dict(zip(ascii_lowercase, h))
word = input().strip()
maxH = max([H[i] for i in word])
area = len(word) * maxH

print(area)
