# Generates testable versions of the lexer/parser,
# then runs the testable version of the parser.

# TODO: test-preamble.sh no longer takes positional arguments

source gen-preamble-test.sh
echo "Build complete..."
source test-preamble.sh $1