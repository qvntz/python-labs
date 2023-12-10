import sys
from collections import deque


def tail(filename: str | None = None, lines: int = 10) -> None:
    if filename:
        with open(file=filename, mode="rt") as f:
            contents = deque(iterable=f, maxlen=lines)
    else:
        contents = deque(iterable=sys.stdin, maxlen=lines)

    for line in contents:
        sys.stdout.write(line)


def main():
    if len(sys.argv) > 1:
        for i, filename in enumerate(iterable=sys.argv[1:], start=1):
            if i > 1:
                print("\n==> %s <==" % filename)
            tail(filename=filename)
    else:
        tail(lines=17)


if __name__ == "__main__":
    main()
