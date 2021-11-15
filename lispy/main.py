import sys

from prompt_toolkit import PromptSession
from tree_sitter import Language, Parser


def evaluate(line: str):
    if line in ["exit", "exit()", "quit", "quit()"]:
        print("Goodbye!")
        sys.exit(0)


def main():
    Language.build_library("data/elisp.so", ["tree-sitter-elisp"])
    ELISP_LANGUAGE = Language("data/elisp.so", "elisp")
    parser = Parser()
    parser.set_language(ELISP_LANGUAGE)
    session: PromptSession[str] = PromptSession()
    while True:
        line: str = session.prompt("prompt-kit: lispy> ")
        evaluate(line)
        tree = parser.parse(bytes(line, "utf8"))
        print(tree.root_node.sexp())
