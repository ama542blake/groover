# see Notation.mnd
from typing import Dict, List, Union
from timesignatureutils import InvalidTimeSignatureException, TimeSignature, parse_time_signature
from music21.stream.base import Stream
from music21.percussion import PercussionChord
from drumset import available_instruments, instrument_descriptors, descriptor_to_string, descriptor_to_notation

# e.g., "{'k': 'x  xx  x'}"
InstrumentAndRhythm = Dict[str, str]
Measure = Stream[PercussionChord]
Groove = Stream[Measure]

# each PercussionChord corresponds to each temporal position within the measure\
# each Stream[PercussionChord] is a measure
# the Stream[Stream[PercussionChord]] is the entire groove
def measures_to_stream(measure_strs: List[InstrumentAndRhythm], time_signature: TimeSignature) -> Groove:
    groove: Groove = Stream()
    for raw_measure in measure_strs:
        measure: Measure = Stream()

        for temporal_idx in range(time_signature.measure_length):
            

        for (part, rhythm) in raw_measure:
            (staff_position, note_head) = descriptor_to_notation[part]
            for note in rhythm:
                if note == ' ':
                    measure




def simple_generator():
    ts_valid: bool = False
    time_sig = None
    while not ts_valid:
        try:
            time_sig: Union[TimeSignature, None] = parse_time_signature(input('Enter a time signature, or hit enter for 4/4\n'))
            ts_valid = True  # parsing will fail if it's not valid
        except InvalidTimeSignatureException:
            continue

    if time_sig is None:
        raise RuntimeError("variable 'time_sig' is None, but it should not be")

    num_measures: int = 0
    while(num_measures < 1):
        try:  # will throw exception if input is not numeric
            num_measures: int = int(input("Enter number of measures\n"))
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


    measures: List[InstrumentAndRhythm] = []  # indices are measure_num - 1
    for measure_idx in range(num_measures):
        for (descriptor_idx, descriptor) in enumerate(to_use):
            this_rhythm = ''
            while len(this_rhythm) != time_sig.measure_length:
                this_rhythm = input(f'Measure {measure_idx + 1} {descriptor_to_string[descriptor]} rhythm: ')
            if descriptor_idx == 0:
                measures.append({descriptor: this_rhythm})
            else:
                measures[measure_idx][descriptor] = this_rhythm

    measures_to_streams(measures)
            
    
    