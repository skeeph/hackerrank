def count_substring(S: str, s: str):
    cnt = 0
    for i in range(0, len(S) - len(s) + 1):
        if S[i:i + len(s)] == s:
            cnt += 1

    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
