from re import sub
import this
from typing import Dict, List, Set, Union
from timesignatureutils import InvalidTimeSignatureException, TemporalProperties, parse_time_signature
from music21.stream.base import Part, Measure
from music21.percussion import PercussionChord
from drumset import Notation, instrument_descriptors, descriptor_to_string, descriptor_to_notation
from music21.note import Note, Rest
from music21.clef import PercussionClef
from music21.meter.base import TimeSignature
from json import dumps

# e.g., "{'k': 'x  xx  x'}"
DescriptorToRhythmMap = Dict[str, str]

def simple_generator() -> Part:
    """
    Guides the user through creating a groove using the simple generator.

    Returns:
        Part: The Part object, which can be rendered as musical notation or further processed.
    """

    temporal_properties: TemporalProperties = _collect_temporal_properties()
    num_measures: int = _collect_num_measures()
    to_use: str = _collect_instruments_to_use()
    measures: List[DescriptorToRhythmMap] = []  # indices are measure_num - 1
    subdivs_per_measure = temporal_properties.subdivisions_per_measure

    print(f'Input your groove. Each measure should have {subdivs_per_measure} notes/rests per part')
    for measure_idx in range(num_measures):
        for (descriptor_idx, descriptor) in enumerate(to_use):
            this_rhythm = ''
            while len(this_rhythm) != subdivs_per_measure:
                this_rhythm = input(f'Measure {measure_idx + 1} {descriptor_to_string[descriptor]} rhythm: ')
            if descriptor_idx == 0:
                measures.append({descriptor: this_rhythm})
            else:
                measures[measure_idx][descriptor] = this_rhythm

    return raw_measures_to_stream(measures, temporal_properties=temporal_properties)


def complex_generator() -> Part:
    """
    Guides the user through creating a groove using the complex generator.
    The complex measure strings are converted into the same format that the
    simple generator produces, before being converted to a Part object.
    
    Returns:
        Part: The Part object, which can be rendered as musical notation or further processed.
    """

    temporal_properties: TemporalProperties = _collect_temporal_properties()
    num_measures: int = _collect_num_measures()
    measures: List[DescriptorToRhythmMap] = []  # indices are measure_num - 1
    subdivs_per_measure = temporal_properties.subdivisions_per_measure

    print(f'Input your groove. Each measure should have {subdivs_per_measure} notes/rests per measure')
    for measure_idx in range(num_measures):
        this_measure = input(f'Measure {measure_idx + 1}: ')
        # TODO: make sure this is correct length
        this_measure_map: DescriptorToRhythmMap = _parse_complex_measure(this_measure)
        measures.append(this_measure_map)

    return _raw_measures_to_stream(measures, temporal_properties=temporal_properties)


def _raw_measures_to_stream(measure_strs: List[DescriptorToRhythmMap], temporal_properties: TemporalProperties) -> Part:
    """
    Takes raw measures (as strings) and converts them to a drum set Part.
    
    The input dictionary mapping descriptors to the string reprresentation of their rhythms should
    have exactly the number of characters are there are subdivisions per measure (which is dictated
    by the passed TemporalProperties argument). Any non-space character represents the presence of
    that instrument at that temporal slice. Space characters represent the lack of presence of an
    instrument at that temporal slice.

    Args:
        measure_strs (List[DescriptorToRhythmMap]): A dictionary mapping from instrument descriptors to their rhythms.
        temporal_properties (TemporalProperties): An object specifying properties about how time is to be divided for the part.

    Returns:
        Part: A Part object that represents the passed set of raw strings.
    """

    groove: Part = Part()

    groove.append(PercussionClef())
    for (measure_idx, measure_dict) in enumerate(measure_strs):
        measure: Measure = Measure()
        if (measure_idx == 0):
            measure.append(temporal_properties.time_signature)

        for subdivision_idx in range(temporal_properties.subdivisions_per_measure):
            this_time_idx_pchord: PercussionChord = PercussionChord(duration=temporal_properties.duration)
            for (instrument, rhythm) in measure_dict.items():
                if (rhythm[subdivision_idx] != ' '):  # is not a rest
                    notation: Notation = descriptor_to_notation[instrument]
                    note: Note = Note(pitch=notation[0])
                    note.notehead = notation[1]
                    this_time_idx_pchord.add(note)
            
            if (len(this_time_idx_pchord) == 0):  # there are no notes at this temporal position
                measure.append(Rest(duration=temporal_properties.duration))
            else:
                measure.append(this_time_idx_pchord)

        groove.append(measure)
    
    return groove


def _collect_temporal_properties() -> TemporalProperties:
    """
    Collects temporal information from the user. Temporal information includes all
    information needed to determine time signature and note duration.

    Returns:
        TemporalProperties: An object specifying temporal information for the groove.
    """

    ts_valid: bool = False
    time_sig = None
    while not ts_valid:
        try:
            time_sig: Union[TimeSignature, None] = parse_time_signature(input('Enter a time signature, or hit enter for 4/4: '))
            ts_valid = True  # parsing in the line above will fail if it's not valid
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
    return TemporalProperties(time_signature=time_sig, subdivide_by=subdivision)


def _collect_num_measures() -> int:
    """
    Asks the user how many measures the groove should be.

    Returns:
        int: The number entered by the user.
    """

    num_measures: int = 0
    while(num_measures < 1):
        try:  # will throw exception if input is not numeric
            num_measures: int = int(input("Enter number of measures: "))
        except:
            continue

    return num_measures


def _collect_instruments_to_use() -> str:
    """
    Asks the user to input which instruments they'd like to include in the groove.
    The user inputs a string of descriptors.
    E.g., 'skh' means that the user wants the groove to consist of snare, kick, and hi-hat.

    Returns:
        str: The descriptor string as entered by the user.
    """

    to_use = ''
    while to_use == '':
        to_use = input(f'Which instruments do you want to use? Your options are:\n{instrument_descriptors}\n')
        for inst in to_use:
            if inst not in instrument_descriptors:
                print(f'"{inst}" is not a valid option')
                to_use = ''  # will force new input

    return to_use


COMPLEX_REST_CHARACTER = '_'  # the character that indicates a rest in the complex mode
COMPLEX_SLICE_CHARACTER = ' '  # the character that specifies the end of a temporal slice in complex mode

def _determine_descriptors_used(complex_measure_str: str) -> Set[str]:
    """
    Intended for use with complex measure strings. Finds the unique set
    of descriptors used so that DescriptorToRhythmMap entries can be initialized.

    Args:
        complex_measure_str (str): The raw complex measure string.

    Returns:
        Set[str]: A unique set of instrument descriptors used in the measure.
    """

    return set(complex_measure_str) - set((COMPLEX_SLICE_CHARACTER, COMPLEX_SLICE_CHARACTER))


def _parse_complex_measure(raw_complex_measure: str) -> DescriptorToRhythmMap:
    """
    Transforms the raw complex measure string into it's DescriptorToRhythmMap.

    Args:
        raw_complex_measure (str): The raw complex measure string.

    Returns:
        DescriptorToRhythmMap: A map from instrument descriptor to its rhythm string.
    """

    # this method doesn't check to make sure length of the measure is correct - assumes this is done elsewhere
    descriptors_used: Set[str] = _determine_descriptors_used(raw_complex_measure)
    mapped = dict.fromkeys(descriptors_used, '')
    # ensure no empty strings in the list (in case extra separator spaces are used)
    parsed_measure = filter(lambda item: item != '', raw_complex_measure.split(' '))
    temporal_slice: Set[str]  # can't annotate in for loop
    for temporal_slice in map(lambda m: set(m), parsed_measure):
        # TODO: make sure '_' can't be snuck in with other descriptors - e.g. 'h_s'
        # the descriptors which ARE used in this temporal slice
        for descriptor in set(temporal_slice) & descriptors_used:
            mapped[descriptor] += 'x'
        # the descriptors which are NOT used in this temporal slice
        for descriptor in descriptors_used - set(temporal_slice):
            mapped[descriptor] += ' '
        
    return mapped
