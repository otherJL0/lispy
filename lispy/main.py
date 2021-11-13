import readline


def evaluate(line: str):
    print(line)


def main():
    while True:
        line: str = input("lispy> ")
        readline.add_history(line)
        evaluate(line)
