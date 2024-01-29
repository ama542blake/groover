lexer grammar PreambleLexer;
import CommonTokensLexer;

PREAMBLE_OPENER: '<|' ;
PREAMBLE_CLOSER: '|>' ;

KW_TITLE: T I T L E COLON ;
KW_COMPOSER: C O M P O S E R COLON ;
KW_TS: ( T S |  T I M E ' ' S I G N A T U R E ) COLON ;
KW_SUBDIV: ( S U B D I V S | S U B D I V B Y | N ) COLON ;