# str_count, word_count, bytes_count
import sys


def wc(filename=None) -> tuple[int, int, int]:
    if filename:
        with open(filename, "r") as file:
            content = file.read()
    else:
        content = sys.stdin.read()

    lines = len(content.split("\n"))
    words = len(content.split())
    chars = len(content)

    return lines, words, chars


if __name__ == "__main__":
    filenames = sys.argv[1:]

    if not filenames:
        lines, words, chars = wc()
        print(f"{lines} {words} {chars}")
    else:
        total_lines, total_words, total_chars = 0, 0, 0
        for filename in filenames:
            lines, words, chars = wc(filename)
            total_lines += lines
            total_words += words
            total_chars += chars
            print(f"{lines} {words} {chars} {filename}")

        if len(filenames) > 1:
            print(f"{total_lines} {total_words} {total_chars} total")
