import sys


def main(arg):
    if arg == 'run':
        return 'Hello World'
    else:
        return 'Goodbye'


if __name__ == "__main__":
    print(main(sys.argv.__getitem__(1)))
