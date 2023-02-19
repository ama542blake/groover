# see Notation.mnd
from timesignatureutils import InvalidTimeSignatureException, TimeSignature, parse_time_signature


available_instruments = 'hcCrRsk123'

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

    # TODO: ask which instruments ought to be part of the groove
    