Next steps:

Here are some general next steps:

<ul>
    <li>Set this up on GitHub</li>
    <li>More fully flesh out the concept of <code>Transformer</code>s and <code>Extractor</code>s. Isthere some kind of hierarchical relationship here that could potentially be turned into a polymorphic class structure?</li>
    <li>Find a test framework</li>
</ul>

The biggest thing to do is to figure out exactly what will be passed
to the <code>ExtractorBase.extract()</code> method. The two main options I see right now are:

<ul>
    <li>
        <a href="https://web.mit.edu/music21/doc/usersGuide/usersGuide_07_chords.html">Chord documentation</a><br>
        A <code>Chord</code> object which contains the notes and *possibly* their stickings.
        The stickings may only be required in some instances, like for example with the
        <code>StickingExtractor</code>, it may be very useful to know the sticking
        of each note in the chord.
    </li>
    <li>
        <a href="https://web.mit.edu/music21/doc/usersGuide/usersGuide_02_notes.html"><Note documentation</a>
        A <code>Note</code>. If this is done, we lose context about what else may have been hit in usison with
        the note passed in. Maybe this isn't important? Before I can tell whether this might be useful, I should
        have a better idea of how and what I might want to do..
    </li>
</ul>
