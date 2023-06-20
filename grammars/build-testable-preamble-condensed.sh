# builds the version of the parser that can be directly tested without integration into the program
antlr4 PreambleCondensed.g4 -o testable/preamblecondensed -no-listener -no-visitor
javac testable/preamblecondensed/*.java