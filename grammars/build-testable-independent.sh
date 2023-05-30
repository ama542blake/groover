# builds the version of the parser that can be directly tested without integration into the program
antlr4 Independent.g4 -o testable/independent -no-listener -no-visitor
javac testable/independent/*.java