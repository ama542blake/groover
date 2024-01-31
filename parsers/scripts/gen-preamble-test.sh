# Generates testable version of the PreambleParser.
# Also generates test version of the lexer.

source gen-test-preamble-tokens.sh
cd ../grammars
antlr4 PreambleParser.g4 -lib ../gen/test/preamble -o ../gen/test/preamble -no-listener -no-visitor
javac ../gen/test/preamble/*.java
cd ../scripts