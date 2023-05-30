grammar Composite;

groove : measure+ EOF ;
measure : ( GROUP_DELIM* note_group GROUP_DELIM* )+  '|'  ;
note_group : NOTE+ | REST ;

WS : [\t\r\n]+ -> skip ;
GROUP_DELIM: ' ';
REST: '_';
NOTE : 'h' | 'c' | 'C' | 'r' | 'R' | 's' | 'k' | '1' | '2' | '3' ;