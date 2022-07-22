from music21.instrument import UnpitchedPercussion

class DrumSet(UnpitchedPercussion):
    """
    https://web.mit.edu/music21/doc/moduleReference/moduleInstrument.html#unpitchedpercussion
    https://github.com/cuthbertLab/music21/blob/4241e5f016bc73c560fa694e7a7a6499ede51dbd/music21/instrument.py#L1111
    """
    def __init__(self):
        self.instrumentName = 'Drumset'
        self.instrumentAbbreviation = 'D Set'
        # TODO: ALL OF THE BELOW ARE COPIED FROM WOODBLOCK... don't understand what these are
        self.instrumentSound = 'percussion.wood-block'
        self.inGMPercMap = True
        self.midiProgram = 115

        self._modifier = ''
        self._modifierToPercMapPitch = {'high': 76, 'low': 77, 'hi': 76, 'lo': 77}
        self._percMapPitchToModifier = {76: 'high', 77: 'low'}
        self.percMapPitch = self._modifierToPercMapPitch[self._modifier]