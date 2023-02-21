from enum import Enum, auto
from typing import Dict, Tuple
from music21.duration import Duration

class InvalidTimeSignatureReason(Enum):
    FORMAT = auto()
    MEASURE_LENGTH = auto()
    SUBDIVISION = auto()


class InvalidTimeSignatureException(Exception):
    def __init__(self, ts_str: str, reason: InvalidTimeSignatureReason):
        reason_str = ''
        if reason == InvalidTimeSignatureReason.FORMAT:
            reason_str = "invalid format"
        elif reason == InvalidTimeSignatureReason.MEASURE_LENGTH:
            reason_str = "measure length must be greater than 1"
        elif reason == InvalidTimeSignatureReason.SUBDIVISION:
            reason_str = "subdivision must be 4, 8, or 16"
            super().__init__(f'{ts_str} is not a valid time signature - {reason_str}')


class TimeSignature:
    _beat_value_to_quarter_length: Dict[int, float] = {
        4: 1.0,
        8: 0.5,
        16: 0.25
    }

    # TODO: there's more here than just time_sig info, maybe spread this out a bit
    def __init__(self, beats: int, beat_value: int, subdivision: int):
        '''
        arguments:
            beats - the top number of the time signature
            beat_value - the bottom number of the time signature
            subdivisions - how many times to divide each beat
        '''
        self.beats = beats
        self.beat_value = beat_value
        self._subdivision = subdivision
        # the number of temporal slots per measure = (beats/measure) * (subdivisions/beat) -> subdivisions/measure
        # or, more simply, the number of notes to collet per part per measure
        self.subdivisions_per_measure = self.beats * subdivision
        # calculate the fraction of a quarter note each subdivion in the measure takes up - used to determine note duration
        self._quarter_length = TimeSignature._beat_value_to_quarter_length[self.beat_value] / self.beats
        self.duration = Duration()
        self.duration.quarterLength = self._quarter_length



def parse_time_signature(ts_str: str) -> TimeSignature:
    if ts_str == '':
        # -1 because the subdivision hasn't been determined yet
        return TimeSignature(4, 4, -1)
    else:
        split = ts_str.replace(' ', '').split('/')
        if len(split) != 2 or not split[0].isnumeric() or not split[1].isnumeric():
            raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.FORMAT)
        else:
            beats = int(split[0])
            if (beats < 3):
                raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.MEASURE_LENGTH)
            
            subdivision = int(split[1])
            if (subdivision not in [4, 8, 16]):
                raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.SUBDIVISION)
            
            return TimeSignature(beats, subdivision, -1)
            