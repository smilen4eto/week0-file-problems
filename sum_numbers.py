from sys import argv
script, filename = argv


def main():
    file = open(filename, 'r')

    f = file.read()

    n = f.split(' ')
    s = 0
    for i in n:
        s = s + int(i)
    print(s)
    pass

if __name__ == '__name__':
    main()
