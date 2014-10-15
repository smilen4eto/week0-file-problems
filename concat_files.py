import sys


def main():
    fn = 'megatron.txt'
    fw = open(fn, 'a')
    for arg in range(1, len(sys.argv)):
        fr = open(sys.argv[arg], 'r')
        new = fr.read()
        fw.write(' '.join(new))
        fr.close()
    fw.close()

if __name__ == '__name__':
    main()
