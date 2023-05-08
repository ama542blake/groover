from generator import complex_generator, simple_generator

SIMPLE_MODE_SELECTOR = 'simple'
COMPLEX_MODE_SELECTOR = 'complex'

if __name__ == "__main__":
    mode_str = input(f"Enter mode - '{SIMPLE_MODE_SELECTOR}' or '{COMPLEX_MODE_SELECTOR}'\n")
    if mode_str == SIMPLE_MODE_SELECTOR:
        simple_generator().show()
    elif mode_str == COMPLEX_MODE_SELECTOR:
        complex_generator().show()

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
