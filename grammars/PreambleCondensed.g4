grammar PreambleCondensed;
/** Must specify at least one of these options if the preamble opener token is present, but the
    order doesn't matter. As a result of this, the grammar permits the same rule to be matched
    multiple times (it is syntactically valid), but when walking the parse tree, a check must be
    done to ensure each of these is only matched once.
 */
// TODO: parse tree walker must ensure that each of these def rules are matched only once
preamble: PREAMBLE_OPENER preambleField+ PREAMBLE_CLOSER;
preambleField: titleDef
    | composerDef
    | tsDef
    | subdivDef
    ;
titleDef: KW_TITLE PREAMBLE_SEP NAME NEWLINE ;  // give the groove a title
composerDef: KW_COMPOSER PREAMBLE_SEP NAME NEWLINE ;  // name the groove's composer
tsDef: KW_TS PREAMBLE_SEP timeSignature NEWLINE ; // specify the time signature
subdivDef: KW_SUBDIV PREAMBLE_SEP subdivs=INT NEWLINE ;
timeSignature: INT '/' INT ;

PREAMBLE_OPENER: '<|' NEWLINE;
WS: [ \t]+ -> skip ;
INT: [0-9]+ ;
NEWLINE: '\r'? '\n' ;

// mode PREAMBLE;
PREAMBLE_SEP : ':' ;
KW_TITLE: 'TITLE' ;
KW_COMPOSER: 'COMPOSER' ;
KW_TS: 'TS' | 'TIME SIGNATURE' ;
KW_SUBDIV: 'SUBDIVS' | 'SUBDIVBY' | 'N' ;
NAME: [a-zA-Z] [a-zA-Z ]* ;
PREAMBLE_CLOSER: '|>' ;