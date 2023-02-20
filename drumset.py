from typing import Dict, Optional, Tuple
from music21.instrument import UnpitchedPercussion
from music21.note import Unpitched, Rest
from music21.duration import Duration

# class DrumSet:
#     def snare(quarter_length: Optional[float] = None) -> Unpitched:
#         return Unpitched('C5', duration=Duration(quarter_length))


#     def hh(quarter_length: Optional[float] = None) -> Unpitched:
#         hh = Unpitched('G5')
#         hh.notehead = "x"
#         return hh


#     def kick(quarter_length: Optional[float] = None) -> Unpitched:
#         return Unpitched('F4')


#     def rest(quarter_length: Optional[float] = None) -> Rest:
#         return Rest()

# https://web.mit.edu/music21/doc/moduleReference/moduleNote.html#music21.note.NotRest.notehead
NOTE_HEAD_NORMAL = 'normal'
NOTE_HEAD_X = 'x'
NOTE_HEAD_CIRCLED_X = 'circle-x'
NOTE_HEAD_TRIANGLE = 'triangle'

# pair of (staff position, note head)
Notation = Tuple[str, str]
# TODO: verify correctness
descriptor_to_notation: Dict[str, Notation] = {
    'h': ('F5', NOTE_HEAD_X),
    'H': ('F5', NOTE_HEAD_CIRCLED_X),
    'c': ('A5', NOTE_HEAD_X),
    'C': ('A5', NOTE_HEAD_CIRCLED_X),
    'r': ('G5', NOTE_HEAD_CIRCLED_X),
    'R': ('G5', NOTE_HEAD_TRIANGLE),
    '1': ('E5', NOTE_HEAD_NORMAL),
    '2': ('D5', NOTE_HEAD_NORMAL),
    '3': ('A4', NOTE_HEAD_NORMAL),
    's': ('C5', NOTE_HEAD_NORMAL),
    'k': ('F4', NOTE_HEAD_NORMAL)
}

available_instruments = 'hcCrRsk123'

# for use in printing out instruction sets to 
instrument_descriptors = '''
'h' - hi-hat
'c' - crash 1
'C' - crash 2
'r' - ride
'R' - ride bell
's' - snare
'k' - kick
'1' - high tom
'2' - mid tom
'3' - floor tom
'''

descriptor_to_string: Dict[str, str] = {
    'h': 'hi-hat',
    'c': 'crash 1',
    'C': 'crash 2',
    'r': 'ride',
    'R': 'ride bell',
    's': 'snare',
    'k': 'kick',
    '1': 'high tom',
    '2': 'mid tom',
    '3': 'floor tom'
}