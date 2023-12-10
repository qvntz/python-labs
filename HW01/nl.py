import sys


def nl(file: str | None = None) -> None:
    if file is not None:
        try:
            with open(file, "r") as f:
                for i, line in enumerate(f, start=1):
                    print(f"\t{i} {line}", end="")
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.", file=sys.stderr)
            sys.exit(1)
        return
    try:
        for i, line in enumerate(sys.stdin, start=1):
            print(f"\t{i} {line}", end="")
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nl()
    else:
        nl(sys.argv[1])
