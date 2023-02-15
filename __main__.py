from drumset import DrumSet as ds
from music21.stream import Stream
from music21.percussion import PercussionChord
from music21.duration import Duration
from music21.note import Rest

if __name__ == "__main__":
    hh = input("Enter the hi-hat rhythm as 8th notes\n")
    snare = input("Enter the snare rhythm as 8th notes\n")
    kick = input("Enter the kick rhythm as 8th notes\n")
    if (len(hh) == len(snare) and len(snare) == len(kick)):
        num_notes = len(hh)
        measure = Stream()
        for i in range(len(hh)):
            has_hh = hh[i] == "x"
            has_snare = snare[i] == "x"
            has_kick = kick[i] == "x"
            if (not has_hh and not has_snare and not has_kick):
                measure.append(ds.rest(quarter_length=0.5))
            else:
                chord_notes = []
                if has_hh:
                    chord_notes.append(ds.hh())
                if has_snare:
                    chord_notes.append(ds.snare())
                if has_kick:
                    chord_notes.append(ds.kick())
                measure.append(PercussionChord(chord_notes, duration=Duration(0.5)))
        measure.show()
    else:
        print("All parts must be same length")
    # Stream(list(map(lambda n: make_hh() if n == "x" else make_rest(), hh))).show()
    # Stream(list(map(lambda n: make_snare() if n == "x" else make_rest(), snare))).show()
    # Stream(list(map(lambda n: make_kick() if n == "x" else make_rest(), kick))).show()
    # print(snare)
    # print(kick)

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
