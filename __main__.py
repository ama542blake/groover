import argparse
from http.client import REQUEST_ENTITY_TOO_LARGE
import sys
from typing import Literal
from generator import complex_generator, simple_generator

INDEPENDENT_PARSER_FLAG = 'i'
COMPOSITE_PARSER_FLAG = 'c'

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog="Groover",
        description='A text-based tool for quick and concise but expressive drum groove transcription.'
    )
    arg_parser.add_argument(
        "parser",
        type=str,
        options=[INDEPENDENT_PARSER_FLAG, COMPOSITE_PARSER_FLAG],
        required=True,
        help='The parser to use.'
    )
    arg_parser.add_argument(
        '--individual', '-i',
        help='When passed, indicates that measures will be asked for one at a time. Only valid with the independent parser.',
        action="store_true"
    )
    arg_parser.parse_args()

    mode: Literal['simple', 'complex'] = arg_parser.mode # type: ignore
    if mode == 'parser':
        simple_generator().show()
    elif mode == 'complex':
        complex_generator.show()
    else:
        sys.exit(1)
    
    # mode_str = input(f"Enter mode - '{SIMPLE_MODE_SELECTOR}' or '{COMPLEX_MODE_SELECTOR}'\n")
    # if mode_str == SIMPLE_MODE_SELECTOR:
    #     simple_generator().show()
    # elif mode_str == COMPLEX_MODE_SELECTOR:
    #     complex_generator().show()

# for extractor
# if __name__ == "__main__":
#     num_args = len(sys.argv) - 1  # -1 because sys.argv[0] is the file name
#     if num_args == 0:
#         print("Must enter a file name")
#         sys.exit(-1)
#     if num_args > 1:  # first arg is file name
#         print("Too many input arguments; must enter a file name")
#         sys.exit(-1)

#     fname = sys.argv[1]
#     if not (fname[-4:] == ".mxl" or fname[-9:] == ".musicxml"):
#         print("File extension must be '.mxl' or '.musicxml'")
#         sys.exit(-1)

#     app.run(fname)


