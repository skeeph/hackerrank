
def print_rangoli(n):
    from string import ascii_lowercase as alphabet
    pattern = [("-".join(alphabet[n - 1: n - i - 1: -1] + alphabet[n - i - 1: n])).center(4 * n - 3, "-") for i in
               range(n)]
    print('\n'.join(pattern[: -1] + pattern[:: -1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
