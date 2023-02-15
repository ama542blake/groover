from music21.note import Unpitched, Rest
from music21.duration import Duration
from music21.converter import parse
from music21.stream import Score, Part
from music21.instrument import UnpitchedPercussion
from music21.percussion import PercussionChord
from sticking_extractor import sticking_extractor

text_to_note = {"x": lambda dur: Unpitched(duration=Duration(dur)), "-": lambda dur: Rest(duration=Duration(dur))}

def get_quarter_length(subdivision, num_divisions):
    """
    Calculates the equivalent quarter note length given the underlying subdivision of the beat, and the number of
    subdivisions of a beat being considered.

    Needed because Duration objects base their durations off of quarter notes.

    :param subdivision: The amount of 
    :param num_divisions:
    :return:
    """
    return num_divisions/subdivision


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sticking_extractor(parse('test_mxml/test69.musicxml'), 'Rl', case_insensitive=False).show()

    # make_hh().show()
    # exit()
    # # time signature
    # ts_in = input("Enter the desired time signature: ")  # raw user input
    # ts_top, ts_bot = map(int, ts_in.split())  # get top/bottom time signature numbers
    # # beat subdivision
    # subdivision = int(input("Enter desired base subdivision (per beat): "))
    # # number of notes to be input per bar
    # notes_per_bar = subdivision * ts_top
    # # number of measures
    # num_measures = int(input("Enter the desired number of measures: "))
    # # line names (a line is one specific part of the drum set)
    # line_names = input("Enter the names of each line: ").split()
    # lines = []

    # for line_name in line_names:
    #     rhythm = input(f"Enter {line_name} rhythm:\n\t").replace(" ", "-")
    #     new_line = (line_name, rhythm)
    #     lines.append(new_line)

    # print()
    # for line_name, rhythm in lines:
    #     print(f"{(line_name + ':').ljust(15)}{rhythm}")

    # create the part object for the drum set
    # drumset = Part()
    # Part: http://web.mit.edu/music21/doc/moduleReference/moduleStreamBase.html#part

    # TODO: learn about meter module http://web.mit.edu/music21/doc/moduleReference/moduleMeterBase.html#module-music21.meter.base
    # TODO: learn about Measures
    # TODO: create Stream of ChordBase objects built from Unpitched objects
    # TODO: learn more about instrument objects, see if there is a drum set
    # TODO: read http://web.mit.edu/music21/doc/moduleReference/moduleMidiPercussion.html?highlight=percussionmap#music21-midi-percussionfr
