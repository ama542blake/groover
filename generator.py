# see Notation.mnd
from typing import Dict, List
from timesignatureutils import InvalidTimeSignatureException, TimeSignature, parse_time_signature


available_instruments = 'hcCrRsk123'

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

# e.g., "{'k': 'x  xx  x'}"
InstrumentAndRhythm = Dict[str, str]

def simple_generator():
    ts_valid: bool = False
    while not ts_valid:
        try:
            time_sig: TimeSignature = parse_time_signature(input('Enter a time signature, or hit enter for 4/4\n'))
            ts_valid = True
        except InvalidTimeSignatureException:
            continue

    num_measures_remaining: int = 0
    while(num_measures_remaining < 1):
        try:  # will throw exception if input is not numeric
            num_measures_remaining: int = int(input("Enter number of measures\n"))
        except:
            continue

    # input a string like "skh" -> snare, kick, hi-hat
    to_use = ''
    while to_use == '':
        to_use = input(f'Which instruments do you want to use? Your options are:\n{instrument_descriptors}\n')
        for inst in to_use:
            if inst not in instrument_descriptors:
                print(f'"{inst}" is not a valid option')
                to_use = ''  # will force new input


    measure_num = 1
    measures: List[InstrumentAndRhythm] = []  # indices are measure_num - 1
    while (num_measures_remaining > 0):
        for descriptor in to_use:
            # TODO: need to do some validation on this as its input (e.g., make sure it's not too long)
            # https://docs.python.org/3/library/readline.html#module-readline
            this_rhythm = input(f'Measure {measure_num} {descriptor_to_string[descriptor]} rhythm: ')

        measure_num += 1
    
    