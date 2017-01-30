def capitalize(string:str)->str:
    return " ".join([i.capitalize() for i in string.split(" ")])


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)