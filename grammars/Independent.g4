grammar Independent;

groove : part+ EOF ;
part : DESCRIPTOR ':' measure+ '\n';
measure : ( NOTE | REST )+ '|' ;

DESCRIPTOR : 'h' | 'c' | 'C' | 'r' | 'R' | 's' | 'k' | '1' | '2' | '3' ;
NOTE: 'x' ;
REST: ' ';