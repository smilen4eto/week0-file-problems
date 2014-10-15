from random import randint
from sys import argv
script, filename, n = argv


def main():
    file = open(filename, 'w+')
    for i in range(0, int(n)):
        nums = randint(1, 10)
        file.write(" ".join(str(nums)))

    file.close()

if __name__ == '__main__':
    main()
