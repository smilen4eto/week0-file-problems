from sys import argv


def main():
    for i in argv:
        if "txt" in i:
            file = open(i, "r")
            print file.read()
            file.close()
            pass

if __name__ == '__main__':
    main()
