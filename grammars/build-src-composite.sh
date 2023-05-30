# builds the version of the parser that can be integrated into the program
antlr4 -Dlanguage=Python3 Composite.g4 -o ../parsers/gen/composite -no-listener -visitor