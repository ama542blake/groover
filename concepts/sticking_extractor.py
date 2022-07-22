from music21 import stream, note, articulations

# TODO: determine how to set accent to be above note... sometimes this sets the accent below

def sticking_extractor(s, desired_stick, case_insensitive=True):
    extracted = stream.Stream()
    if case_insensitive:
        desired_stick = desired_stick.lower()

    part = s.getElementsByClass(stream.Part)[0]
    measures = part.getElementsByClass(stream.Measure)
    for measure in measures:
        # TODO: need to get rests also
        notes = measure.getElementsByClass(note.Unpitched)
        for n in notes:
            # TODO: handle case where there isn't just a single lyric
            stick = n.lyrics[0].text
            if case_insensitive:
                stick = stick.lower()

            if stick in desired_stick:
                # TODO, force accent to be above note
                extracted.append(n)
            else:
                # in this case, we need to add a rest
                extracted.append(note.Rest(quarterLength=n.quarterLength))

    return extracted
