lexer grammar PreambleTokens;

PREAMBLE_OPENER: '<|' NEWLINE -> mode(PREAMBLE);
WS: [ \t]+ -> skip ;
INT: [0-9]+ ;
NEWLINE: '\r'? '\n' ;

mode PREAMBLE;
KW_TITLE: 'TITLE:' WS* ;
KW_COMPOSER: 'COMPOSER:' WS* ;
KW_TS: ( 'TS' | 'TIME SIGNATURE' ) ':' WS* ;
KW_SUBDIV: ( 'SUBDIVS' | 'SUBDIVBY' | 'N' ) ':' WS* ;
NAME: ~[\r\n] ;
PREAMBLE_CLOSER: '|>' -> mode(DEFAULT_MODE) ;