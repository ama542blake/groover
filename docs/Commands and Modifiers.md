# Commands and Modifiers
"Commands" are operations that manipulate the groove in some way. For example, there may be a command to repeat the previous measure, or to change the time signature.
"Modifiers", on the other hand, affect only (a) specific note(s). For example, accents and buzzes are modifiers.
Both commands and modifiers can be thought of as functions. They take some input, make some kind of change to them, and return the result. For example, a command to change time signature would take a measure as input, and return that measure with the new time signature. Or, an accent modifier on a note takes that note and returns a new note with an accent.

## To figure out about notation/modifiers
- Need a different syntax for commands and modifiers
- Can commands be applied to multiple measures?
- Can modifiers be applied to multiple notes?
- Where can modifiers and commands appear?
    - Does this depend on the specific command/modifier?
- Will the usage of both of these constructs be supported in both notation modes?
    - If so, will they need to be used differenly between these modes
    - Will the semantics of each command or modifier need to change depending on the context?
- Are there different subtypes of commands and modifiers?
    - E.g., commands to change time signature seem fundamentally different than commands to repeat previous measures

<h2>List of commands:</h2>
- Must be done at very beginning of measure
    - Repeat previous measure
        :rp:
    - Repeat n previous measures
        :rp(n):
    - Copy previous measure with replacement from beat x to beat y
        - E.g. copy the previous measure, but change beats 3 and 4
        - TODO: how to specify beat? Does it need to be done by subdivision index?
        :cp(3,4):<replacement for beats 3 and 4>
    - Copy measure n
        :cp(n):
    - Copy measure n with replacement from beat x to beat y
        :cp(n, x, y)<replacement for beats 3 and 4>:
    - Change time signature
        :ts(num, denom):
    - Change tempo
        :tempo(new_tempo):
- Can be done at any point in the measure
    - Change subdivision (for n beats optionally)
        :subdiv(num_divs[, n]):

<h2>List of modifiers:</h2>
- Applies over multiple beats (by instrument?)
    - Crescendo from beat x to y
    - TODO: how to specify beat? Does it need to be done by subdivision index?
    - TODO: What if it should span multiple measures?
        :cresc(x, y, target_dynamic):
    - Decrescendo from beat x to y
        - TODO: how to specify beat? Does it need to be done by subdivision index?
        - TODO: What if it should span multiple measures?
            :cresc(x, y, target_dynamic):
- Applies to next note (by instrument?)
    - Accent
        :accent:

    - Tenuto
        :tenuto:
    - Flam
        :flam:
    - Drag
        :drag:
    - Ghost note
        :ghost:
    - Buzz
        :buzz:
    - Double stroke
        :double:

## Potential problems with this design
- The paradigm of entering one measure at a time may be difficult
- The paradign of entering one instrument at a time may be confusing (what happens if you are enterning notes for snare/kick/hh, and choose to repeat a measure when entering the snare rhythm? Does each instrument repeat?)