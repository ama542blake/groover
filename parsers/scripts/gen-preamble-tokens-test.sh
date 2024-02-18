# Generates testable version of the PreambleLexer.
# Should not be used directly, but only from gen-preamble-test.sh

cd $GROOVER_ROOT/parsers/grammars
antlr4 PreambleLexer.g4 -o ../gen/test/preamble
cd $GROOVER_ROOT/parser/scripts