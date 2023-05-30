# builds the version of the parser that can be directly tested without integration into the program
antlr4 Composite.g4 -o testable/composite -no-listener -no-visitor
javac testable/composite/*.java