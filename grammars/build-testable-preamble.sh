# builds the version of the parser that can be directly tested without integration into the program
source build-testable-preamble-tokens.sh
antlr4 Preamble.g4 -lib testable/preamble -o testable/preamble -no-listener -no-visitor
javac testable/preamble/*.java