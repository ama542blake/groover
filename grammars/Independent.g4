grammar Independent;

groove : constituentPart+ EOF ;
constituentPart : CONSTITUENT_DESCRIPTOR ':' measure+ '\n';
measure : ( NOTE | REST )+ '|' ;

CONSTITUENT_DESCRIPTOR : 'h' | 'c' | 'C' | 'r' | 'R' | 's' | 'k' | '1' | '2' | '3' ;
NOTE: 'x' ;
REST: ' ';