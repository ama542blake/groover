from generator import simple_generator

if __name__ == "__main__":
    simple_generator().show()

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
