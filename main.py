import sys
from antlr4 import *

from documentadorListener import DocumentadorListener
from gen.Python3Lexer import Python3Lexer
from gen.Python3Parser import Python3Parser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    listener = DocumentadorListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.imprimir()



if __name__ == '__main__':
    main(sys.argv)
