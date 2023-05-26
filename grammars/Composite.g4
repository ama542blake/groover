grammar Composite;

groove : measure+ EOF ;
measure : ( NOTE | REST )+ '|' ;

WS : [ \t\r\n]+ -> skip ; 
NOTE : 'h' | 'c' | 'C' | 'r' | 'R' | 's' | 'k' | '1' | '2' | '3' ;
REST: '_';