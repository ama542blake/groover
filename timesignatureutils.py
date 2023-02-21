from enum import Enum, auto
from typing import Dict, Tuple
from music21.duration import Duration
from music21.meter.base import TimeSignature

class InvalidTimeSignatureReason(Enum):
    FORMAT = auto()
    MEASURE_LENGTH = auto()
    BEAT_VALUE = auto()


class InvalidTimeSignatureException(Exception):
    def __init__(self, ts_str: str, reason: InvalidTimeSignatureReason):
        reason_str = ''
        if reason == InvalidTimeSignatureReason.FORMAT:
            reason_str = "invalid format"
        elif reason == InvalidTimeSignatureReason.MEASURE_LENGTH:
            reason_str = "measure length must be greater than 1"
        elif reason == InvalidTimeSignatureReason.BEAT_VALUE:
            reason_str = "beat value must be 4, 8, or 16"
            super().__init__(f'{ts_str} is not a valid time signature - {reason_str}')


def parse_time_signature(ts_str: str) -> TimeSignature:
    if ts_str == '':
        # -1 because the subdivision hasn't been determined yet
        return TimeSignature('4/4')
    else:
        split = ts_str.replace(' ', '').split('/')
        if len(split) != 2 or not split[0].isnumeric() or not split[1].isnumeric():
            raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.FORMAT)
        else:
            beats = int(split[0])
            if (beats < 3):
                raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.MEASURE_LENGTH)
            
            beat_value = int(split[1])
            if (beat_value not in [4, 8, 16]):
                raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.BEAT_VALUE)
            
            return TimeSignature(f'{beats}/{beat_value}')
        

class TemporalProperties:
    _beat_value_to_quarter_length: Dict[int, float] = {
        4: 1.0,
        8: 0.5,
        16: 0.25
    }

    def __init__(self, time_signature: TimeSignature, subdivide_by: int):
        self.time_signature = time_signature
        if self.time_signature.numerator is None:
            raise Exception("Numerator of time signature can't be NONE")
        if self.time_signature.denominator is None:
            raise Exception("Denominator of time signature can't be NONE")
        self._subdivide_by = subdivide_by 
        # the number of temporal slots per measure = (beats/measure) * (subdivisions/beat) -> subdivisions/measure
        # or, more simply, the number of notes to collet per part per measure
        self.subdivisions_per_measure = self.time_signature.numerator * self._subdivide_by
        # calculate the fraction of a quarter note each subdivion in the measure takes up - used to determine note duration
        self._quarter_length = TemporalProperties._beat_value_to_quarter_length[self.time_signature.denominator] / self.time_signature.numerator
        self.duration = Duration(quarterLength=self._quarter_length)

            