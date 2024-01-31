# builds the version of the parser that can be integrated into the program
antlr4 -Dlanguage=Python3 Independent.g4 -o ../parsers/gen/independent -no-listener -visitor