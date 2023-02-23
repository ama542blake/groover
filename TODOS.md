# General
- Figure out how to set the project up to support type checking (select one of the options below)
  - Pyright: https://github.com/microsoft/pyright/blob/main/docs/getting-started.md
  - MyPy: https://mypy-lang.org/
- Devise structure for project: https://docs.python-guide.org/writing/structure/
  - Fit existing things within this structure

# Generation
  - Document the syntax
  - Support tupletsd
  - Assess feasibility/utility of the command list below
  - Add commands
    - Repeat previous measure for part
      - verbatim
      - replace some part of the previous measure (e.g., beat 1->3 is different)
    - Repeat *n* previous measures for a part
      - verbatim
      - replace some part of the previous measures (e.g., measure 3->beat 3 of measure 4 is different)
    - Repeat previous measure for all parts
      - verbatim
      - replace some part of the previous measure (e.g., beat 1->3 is different)
    - verbatim
      - replace some part of the previous measures (e.g., measure 3->beat 3 of measure 4 is different)
    - Change time signature
    - Change subdivison
      - Permanently
      - For some amount of time (e.g., groove is generally 8th note, but beat 4 should be an 8th note triplet)
  - Document commands
  - Document the "Simple" generator mode
  - Implement the "Chord" generator mode
  
# Extraction
<ul>
    <li>More fully flesh out the concept of <code>Transformer</code>s and <code>Extractor</code>s. Isthere some kind of hierarchical relationship here that could potentially be turned into a polymorphic class structure?</li>
    <li>Find a test framework</li>
</ul>

