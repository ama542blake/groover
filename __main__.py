import argparse
from http.client import REQUEST_ENTITY_TOO_LARGE
import sys
from typing import Literal
from generator import simple_continuous_generator, _simple_serial_generator, complex_generator, simple_generator, simple_serial_generator

INDEPENDENT_PARSER_FLAG = 'i'
COMPOSITE_PARSER_FLAG = 'c'

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog="Groover",
        description='A text-based tool for quick and concise but expressive drum groove transcription.'
    )
    arg_subparser = arg_parser.add_subparsers()
    arg_parser.add_argument(
        "parser",
        type=str,
        choices=[INDEPENDENT_PARSER_FLAG, COMPOSITE_PARSER_FLAG],
        required=True,
        help='The parser to use.'
    )
    v_parser = arg_subparser.add_parser('v')
    v_parser.add_argument(
        '--vertical', '-v',
        help='When passed, indicates that measures will be asked for one at a time. Only valid with the independent parser.',
        action="store_true"
    )
    arg_parser.parse_args()

    # 'i': individual parser - 'c': composite parser
    mode: Literal['i', 'c'] = arg_parser.parser  # type: ignore
    if mode == 'i':
        print('individual')
        if (arg_parser.individual): # type: ignore
            raise NotImplementedError("Individual parser has not yet been implemented")
            
            # simple_serial_generator().show()
        else:
            raise NotImplementedError("Composite parser has not yet been implemented")
            simple_continuous_generator().show()
    elif mode == 'c':
        print("Composite")
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


