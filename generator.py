# see Notation.mnd
from re import sub
from typing import Dict, List, Union
from timesignatureutils import InvalidTimeSignatureException, TemporalProperties, parse_time_signature
from music21.stream.base import Stream
from music21.percussion import PercussionChord
from drumset import Notation, available_instruments, instrument_descriptors, descriptor_to_string, descriptor_to_notation
from music21.note import Note, Rest
from music21.clef import PercussionClef
from music21.meter.base import TimeSignature
from json import dumps

# e.g., "{'k': 'x  xx  x'}"
InstrumentAndRhythm = Dict[str, str]
Measure = Stream[Union[PercussionChord, Rest]]
Groove = Stream[Measure]

# each PercussionChord corresponds to each temporal position within the measure\
# each Stream[PercussionChord] is a measure
# the Stream[Stream[PercussionChord]] is the entire groove
def raw_measures_to_stream(measure_strs: List[InstrumentAndRhythm], temporal_properties: TemporalProperties) -> Groove:
    # TODO: Utilize the music 21 built in measure
    # TODO: add time sig and clef to the first Measure
    groove: Groove = Stream()

    groove.append(PercussionClef())
    for measure_dict in measure_strs:
        measure: Measure = Stream()

        for subdivision_idx in range(temporal_properties.subdivisions_per_measure):
            this_time_idx_pchord: PercussionChord = PercussionChord()
            for (instrument, rhythm) in measure_dict.items():
                if (rhythm[subdivision_idx] != ' '):  # is not a rest
                    notation: Notation = descriptor_to_notation[instrument]
                    note: Note = Note(pitch=notation[0])
                    note.notehead = notation[1]
                    note.duration = temporal_properties.duration
                    this_time_idx_pchord.add(note)
            
            if (len(this_time_idx_pchord) == 0):  # there are no notes at this temporal position
                measure.append(Rest(duration=temporal_properties.duration))
            else:
                measure.append(this_time_idx_pchord)

        groove.append(measure)
    
    return groove


def simple_generator() -> Groove:
    # TODO: refactor collection of temporal properties elsewhere
    ts_valid: bool = False
    time_sig = None
    while not ts_valid:
        try:
            time_sig: Union[TimeSignature, None] = parse_time_signature(input('Enter a time signature, or hit enter for 4/4: '))
            ts_valid = True  # parsing will fail if it's not valid
        except InvalidTimeSignatureException:
            continue
    assert time_sig is not None

    subdivision = -1
    while subdivision < 1:
        try:
            # will throw exception if it can't be cast to int
            subdivision = int(input('How many subdivisions per beat? '))
        except:
            subdivision = -1

    # add the subdivision to the time signature

    temporal_properties: TemporalProperties = TemporalProperties(time_signature=time_sig, subdivide_by=subdivision)

    num_measures: int = 0
    while(num_measures < 1):
        try:  # will throw exception if input is not numeric
            num_measures: int = int(input("Enter number of measures: "))
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

    print(f'Input your groove. Each measure should have {temporal_properties.subdivisions_per_measure} notes/rests per part')
    for measure_idx in range(num_measures):
        for (descriptor_idx, descriptor) in enumerate(to_use):
            this_rhythm = ''
            while len(this_rhythm) != temporal_properties.subdivisions_per_measure:
                this_rhythm = input(f'Measure {measure_idx + 1} {descriptor_to_string[descriptor]} rhythm: ')
            if descriptor_idx == 0:
                measures.append({descriptor: this_rhythm})
            else:
                measures[measure_idx][descriptor] = this_rhythm

    return raw_measures_to_stream(measures, temporal_properties=temporal_properties)
    