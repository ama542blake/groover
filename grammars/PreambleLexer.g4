lexer grammar PreambleLexer;

// TODO: need to refactor some of this stuff to more general files (e.g., INT is globally applicable)

PREAMBLE_OPENER: '<|' -> mode(PREAMBLE);
INT: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
TS_DIVIDER: '/' ;

fragment A: [Aa] ;
fragment B: [Bb] ;
fragment C: [Cc] ;
fragment D: [Dd] ;
fragment E: [Ee] ;
fragment F: [Ff] ;
fragment G: [Gg] ;
fragment H: [Hh] ;
fragment I: [Ii] ;
fragment J: [Jj] ;
fragment K: [Kk] ;
fragment L: [Ll] ;
fragment M: [Mm] ;
fragment N: [Nn] ;
fragment O: [Oo] ;
fragment P: [Pp] ;
fragment Q: [Qq] ;
fragment R: [Rr] ;
fragment S: [Ss] ;
fragment T: [Tt] ;
fragment U: [Uu] ;
fragment V: [Vv] ;
fragment W: [Ww] ;
fragment X: [Xx] ;
fragment Y: [Yy] ;
fragment Z: [Zz] ;
fragment COLON: ':' ;
fragment SPACE: ' ' ;

mode PREAMBLE;
KW_TITLE: T I T L E COLON ;
KW_COMPOSER: C O M P O S E R COLON ;
KW_TS: ( T S |  T I M E SPACE S I G N A T U R E ) COLON ;
KW_SUBDIV: ( S U B D I V S | S U B D I V B Y | N ) COLON ;
NAMED_ITEM: ~[\r\n]+ ;
PREAMBLE_CLOSER: '|>' -> mode(DEFAULT_MODE) ;
