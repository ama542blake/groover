from typing import Dict, Tuple

NOTE_HEAD_NORMAL = 'normal'
NOTE_HEAD_X = 'x'
NOTE_HEAD_CIRCLED_X = 'circle-x'
NOTE_HEAD_TRIANGLE = 'triangle'

# pair of (staff position, note head)
Notation = Tuple[str, str]
# TODO: verify correctness
short_descriptor_to_notation: Dict[str, Notation] = {
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

# e.g., "{'k': 'x  xx  x'}"
ShortDescriptorToRhythmMap = Dict[str, str]

# used when printing list of available instruments to user
short_descriptor_info = '''
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

short_descriptor_to_full: Dict[str, str] = {
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

MEASURE_DELIMITER = '|'