from sys import stdin
from typing import Union
from antlr4 import FileStream, InputStream, CommonTokenStream
from gen.independent.IndependentLexer import IndependentLexer
from gen.independent.IndependentParser import IndependentParser
from parsers.gen.independent_generator_visitor import IndependentGeneratorVisitor

class IndependentParserRunner():
    def __init__(self, filePath: Union[str, None]) -> None:
        input_stream: Union[FileStream, InputStream]
        if filePath:
            input_stream = FileStream(filePath)
        else:
            input_stream = InputStream("TODO:")
        lexer = IndependentLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = IndependentParser(stream)
        groove_tree: IndependentParser.GrooveContext = parser.groove()
        generator: IndependentGeneratorVisitor = IndependentGeneratorVisitor(groove_tree)
        groove_tree.accept(generator).show()



        
