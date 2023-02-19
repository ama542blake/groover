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


_subdivision_to_quater_length: Dict[int, float] = {
    4: 1.0,
    8: 0.5,
    16: 0.25
}


class TimeSignature:
    def __init__(self, ts_tuple: Tuple[int, int]):
        self.measure_length = ts_tuple[0]
        self._quarter_length = _subdivision_to_quater_length[ts_tuple[1]]
        self.duration = Duration(self._quarter_length)


def parse_time_signature(ts_str: str) -> TimeSignature:
    if ts_str == '':
        return TimeSignature((4, 4))
    else:
        split = ts_str.replace(' ', '').split('/')
        if len(split) != 2 or not split[0].isnumeric() or not split[0].isnumeric():
            raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.FORMAT)
        else:
            measure_length = int(split[0])
            if (measure_length < 3):
                raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.MEASURE_LENGTH)
            
            subdivision = int(split[1])
            if (subdivision not in [4, 8, 16]):
                raise InvalidTimeSignatureException(ts_str, InvalidTimeSignatureReason.SUBDIVISION)
            
            return TimeSignature((measure_length, subdivision))
            

