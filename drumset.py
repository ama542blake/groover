from typing import Optional
from music21.instrument import UnpitchedPercussion
from music21.note import Unpitched, Rest
from music21.duration import Duration

class DrumSet:
    def snare(quarter_length: Optional[float] = None) -> Unpitched:
        return Unpitched('C5', duration=Duration(quarter_length))


    def hh(quarter_length: Optional[float] = None) -> Unpitched:
        hh = Unpitched('G5')
        hh.notehead = "x"
        return hh


    def kick(quarter_length: Optional[float] = None) -> Unpitched:
        return Unpitched('F4')


    def rest(quarter_length: Optional[float] = None) -> Rest:
        return Rest()
