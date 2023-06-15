grammar Independent;
import Preamble;

groove: preamble? constituentPart+ EOF ;
constituentPart : CONSTITUENT_DESCRIPTOR ':' measure+  NEWLINE ;
measure : ( NOTE | REST )+ '|' ;

CONSTITUENT_DESCRIPTOR : 'h' | 'c' | 'C' | 'r' | 'R' | 's' | 'k' | '1' | '2' | '3' ;
NOTE: 'x' ;
REST: ' ';