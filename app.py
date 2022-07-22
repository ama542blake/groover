from music21.converter import parse
from groover.extractors.extractor import ExtractorTest

def run(fname):
    # parsed_mxml = parse(fname)
    e = ExtractorTest()
    e.extract()
