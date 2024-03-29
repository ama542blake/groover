lexer grammar CommonTokensLexer;

WS: [ \t]+ -> skip ;
NEWLINE:'\r'? '\n' -> skip;
INT: [0-9]+ ;

TS_DIVIDER: '/' ;
COLON: ':' ;

// alternation required to allow spaces in the middle, but not allow token to end with space 
NAMED_ITEM: [a-zA-Z0-9] ( [a-zA-Z0-9 ]* [a-zA-Z0-9] | [a-zA-Z0-9]* ) ;

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