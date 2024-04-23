// 2110992 VU LAM HOANG DAI
grammar ZCode;

@lexer::header {
from lexererr import *

}

options {
	language=Python3;
}

//-------------- Recognizer -----------------
program: NEWLN* program_stm EOF;
program_stm:  declare_stm program_stm | declare_stm;
declare_stm: variables ignore | function ;

// 6. Variable and function
variables: keyword_var | normal_var | dynamic_var; 
keyword_var: normal_typ_name ID (SLB num_list SRB)? (ASG expression)? ;
normal_var: VAR ID ASG expression ;
dynamic_var: DYNAMIC ID (ASG expression)?;
num_list: NUM_LIT COMMA num_list | NUM_LIT;
parameter: normal_typ_name ID (SLB num_list SRB)?;
function: FUNC ID CLB param_list? CRB (ignore? func_control_stm | ignore);
param_list: parameter COMMA param_list | parameter;

// 7. Statement
stm_list: statement stm_list | ; 
statement: declare_part_stm | asg_stm | flow_control_stm | func_control_stm ;
declare_part_stm: var_stm | func_stm ;
flow_control_stm: if_stm | for_stm | break_stm | continue_stm ;
func_control_stm: return_stm | block_stm;
var_stm: variables ignore;
func_stm: ID CLB expr_list? CRB ignore;
asg_stm: ID (SLB expr_list SRB)? ASG expression ignore;
//if_stm:  IF CLB expression CRB ignore? statement elif_stm? ignore?;
//elif_stm: ELIF CLB expression CRB ignore? statement ignore? elif_stm? | ELSE statement ignore?;
if_stm: IF CLB expression CRB ignore? statement elif_stm (ELSE statement)? ignore?;
elif_stm: ELIF CLB expression CRB ignore? statement elif_stm | ;
for_stm: FOR ID UNTIL expression BY expression ignore? statement ignore?;
break_stm: BREAK ignore;
continue_stm: CONTINUE ignore;
return_stm: RETURN expression? ignore;
block_stm: BEGIN ignore stm_list END ignore;

// 5. Expression
expr_list: expression COMMA expr_list | expression;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (RES | EQL | UEQL | GT | GTE | LT | LTE) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: (ADD | SUB) expression6 | expression7;
expression7: (ID | ID CLB index_operators? CRB) SLB index_operators SRB | expression8;
expression8: ID | typ | sub_expr | func_call;

sub_expr: CLB expression CRB;
func_call: ID CLB expr_list? CRB;
index_operators : expression | expression COMMA index_operators;

// 4. Type and value
typ: NUM_LIT | BOOL_LIT | STR_LIT | arr_lit;
normal_typ_name: NUMBER | BOOL | STRING;
arr_lit: SLB expr_list SRB;


//-------------- Lexical -----------------
// 3.7 Literals
NUM_LIT: DIGIT+ ('.' DIGIT*)? ([Ee] [+-]? DIGIT+)?;
fragment DIGIT: [0-9];
BOOL_LIT: TRUE | FALSE;
STR_LIT:'"' CHAR* '"' {self.text = self.text[1:-1];};
fragment CHAR: (~[\n\r\f\\"] | '\\' [btnfr'\\] | '\'"');

// 3.1 Characters set
ignore: NEWLN (CMT NEWLN | NEWLN)*;
NEWLN: '\n';

// 3.2 Comments
CMT: '##' ~[\r\n\f]* -> skip; 

// 3.4 Keywords
TRUE: 'true';
FALSE: 'false';	
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';


// 3.5 Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
RES: '=';
ASG: '<-';
UEQL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '...';
EQL: '==';

// 3.6 Separators
CLB: '(';
CRB: ')';
SLB: '[';
SRB: ']';
COMMA: ',';


// 3.3 Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \t\r\f\b]+ -> skip ;
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' CHAR* ( '\r\n' | '\n' | EOF ) {
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
	elif(self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' CHAR* ILL_CHAR {
    y = str(self.text)
    raise IllegalEscape(y[1:])
};
fragment ILL_CHAR: '\\' ~[btnfr'\\]| '\\';
