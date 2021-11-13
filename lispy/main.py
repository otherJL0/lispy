def evaluate(line: str):
    print(line)


def main():
    while True:
        read_line: str = input("lispy> ")
        evaluate(read_line)
