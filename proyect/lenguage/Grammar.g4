grammar Grammar;
program:(statement NEWLINE)* EOF;

statement:assing|print|if_statement|for_statement; 

/*definicion de la asignacion */
assing:ID'='expr;

/*definicion de print */
print:'print''('expr')';

/*definicion de if */
if_statement:'if''('expr')'block;

/*definicion de FOR */
for_statement:'for''('assing';'expr';'assing';'')'block;

/*Definicion de block */
block:'{'(statement NEWLINE)*'}';

/*definimos Expr */
expr:expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | expr op=('<'|'>'|'>='|'<=') expr
    | expr op=('=='|'!=') expr
    | ID
    | '('expr')'
    ;

/*Definiicion de elementos finales */

/*Definicion de ID */
ID:[a-zA-Z][a-zA-Z_0-9]*;

/*Definicion de NewLine (saltos de linea o tabulaciones) */
NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';