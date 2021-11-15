import sys

from prompt_toolkit import PromptSession


def evaluate(line: str):
    if line in ["exit", "exit()", "quit", "quit()"]:
        print("Goodbye!")
        sys.exit(0)
    print(line)


def main():
    session: PromptSession[str] = PromptSession()
    while True:
        line: str = session.prompt("prompt-kit: lispy> ")
        evaluate(line)
