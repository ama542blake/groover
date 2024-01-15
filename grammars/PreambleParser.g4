parser grammar PreambleParser;
options { tokenVocab = PreambleLexer; }

/** Must specify at least one of these options if the preamble opener token is present, but the
    order doesn't matter. As a result of this, the grammar permits the same rule to be matched
    multiple times (it is syntactically valid), but when walking the parse tree, a check must be
    done to ensure each of these is only matched once.
 */
// TODO: parse tree walker must ensure that each of these def rules are matched only once
preamble: PREAMBLE_OPENER preambleField+ PREAMBLE_CLOSER ;
preambleField: titleDef
    | composerDef
    | tsDef
    | subdivDef
    ;
titleDef: KW_TITLE NAMED_ITEM ;  // give the groove a title
composerDef: KW_COMPOSER NAMED_ITEM ;  // name the groove's composer
tsDef: KW_TS timeSignature; // specify the time signature
subdivDef: ( KW_SUBDIV subdivs=INT ) ;
timeSignature: INT TS_DIVIDER INT ;
