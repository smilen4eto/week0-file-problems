from sys import argv


script, filename = argv


def main():
    pass
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()

if __name__ == '__main__':
    main()
