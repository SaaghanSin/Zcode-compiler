from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # program: NEWLN* program_stm EOF
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.program_stm()))

    # program_stm:  declare_stm program_stm | declare_stm
    def visitProgram_stm(self, ctx: ZCodeParser.Program_stmContext):
        if ctx.program_stm():
            return [self.visit(ctx.declare_stm())] + self.visit(ctx.program_stm())
        return [self.visit(ctx.declare_stm())]

    # declare_stm: variables ignore | function
    def visitDeclare_stm(self, ctx: ZCodeParser.Declare_stmContext):
        if ctx.variables():
            return self.visit(ctx.variables())
        return self.visit(ctx.function())

    # variables: keyword_var | normal_var | dynamic_var
    def visitVariables(self, ctx: ZCodeParser.VariablesContext):
        if ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        elif ctx.normal_var():
            return self.visit(ctx.normal_var())
        return self.visit(ctx.dynamic_var())

    # keyword_var: normal_typ_name ID (SLB num_list SRB)? (ASG expression)?
    def visitKeyword_var(self, ctx: ZCodeParser.Keyword_varContext):
        if ctx.num_list():
            if ctx.expression():
                return VarDecl(
                    Id(ctx.ID().getText()),
                    ArrayType(
                        self.visit(ctx.num_list()), self.visit(ctx.normal_typ_name())
                    ),
                    None,
                    self.visit(ctx.expression()),
                )
            return VarDecl(
                name=Id(ctx.ID().getText()),
                varType=ArrayType(
                    self.visit(ctx.num_list()), self.visit(ctx.normal_typ_name())
                ),
            )
        elif ctx.expression():
            return VarDecl(
                name=Id(ctx.ID().getText()),
                varType=self.visit(ctx.normal_typ_name()),
                varInit=self.visit(ctx.expression()),
            )
        return VarDecl(
            name=Id(ctx.ID().getText()), varType=self.visit(ctx.normal_typ_name())
        )

    # normal_var: VAR ID ASG expression ;
    def visitNormal_var(self, ctx: ZCodeParser.Normal_varContext):
        return VarDecl(
            Id(ctx.ID().getText()), None, "var", self.visit(ctx.expression())
        )

    # dynamic_var: DYNAMIC ID (ASG expression)?;
    def visitDynamic_var(self, ctx: ZCodeParser.Dynamic_varContext):
        if ctx.expression():
            return VarDecl(
                Id(ctx.ID().getText()), None, "dynamic", self.visit(ctx.expression())
            )
        return VarDecl(Id(ctx.ID().getText()), None, "dynamic", None)

    # num_list: NUM_LIT COMMA num_list | NUM_LIT
    def visitNum_list(self, ctx: ZCodeParser.Num_listContext):
        if ctx.num_list():
            return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.num_list())
        return [float(ctx.NUM_LIT().getText())]

    # parameter: normal_typ_name ID (SLB num_list SRB)?
    def visitParameter(self, ctx: ZCodeParser.ParameterContext):
        if ctx.num_list():
            return [
                VarDecl(
                    Id(ctx.ID().getText()),
                    ArrayType(
                        self.visit(ctx.num_list()),
                        self.visit(ctx.normal_typ_name()),
                    ),
                )
            ]
        return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.normal_typ_name()))]

    # function: FUNC ID CLB param_list? CRB (ignore? func_control_stm | ignore)
    def visitFunction(self, ctx: ZCodeParser.FunctionContext):
        if ctx.param_list():
            if ctx.func_control_stm():
                return FuncDecl(
                    Id(ctx.ID().getText()),
                    self.visit(ctx.param_list()),
                    self.visit(ctx.func_control_stm()),
                )
            else:
                return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.param_list()))
        if ctx.func_control_stm():
            return FuncDecl(
                Id(ctx.ID().getText()),
                [],
                self.visit(ctx.func_control_stm()),
            )
        return FuncDecl(Id(ctx.ID().getText()), [])

    # param_list: parameter COMMA param_list | parameter
    def visitParam_list(self, ctx: ZCodeParser.Param_listContext):
        if ctx.param_list():
            return self.visit(ctx.parameter()) + self.visit(ctx.param_list())
        return self.visit(ctx.parameter())

    # stm_list: statement stm_list | ;
    def visitStm_list(self, ctx: ZCodeParser.Stm_listContext):
        if ctx.stm_list():
            return [self.visit(ctx.statement())] + self.visit(ctx.stm_list())
        return []

    # statement: declare_part_stm | asg_stm | flow_control_stm | func_control_stm
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        if ctx.declare_part_stm():
            return self.visit(ctx.declare_part_stm())
        elif ctx.asg_stm():
            return self.visit(ctx.asg_stm())
        elif ctx.flow_control_stm():
            return self.visit(ctx.flow_control_stm())
        return self.visit(ctx.func_control_stm())

    # declare_part_stm: var_stm | func_stm
    def visitDeclare_part_stm(self, ctx: ZCodeParser.Declare_part_stmContext):
        if ctx.var_stm():
            return self.visit(ctx.var_stm())
        return self.visit(ctx.func_stm())

    # flow_control_stm: if_stm | for_stm | break_stm | continue_stm
    def visitFlow_control_stm(self, ctx: ZCodeParser.Flow_control_stmContext):
        if ctx.if_stm():
            return self.visit(ctx.if_stm())
        elif ctx.for_stm():
            return self.visit(ctx.for_stm())
        elif ctx.break_stm():
            return self.visit(ctx.break_stm())
        return self.visit(ctx.continue_stm())

    # func_control_stm: return_stm | block_stm
    def visitFunc_control_stm(self, ctx: ZCodeParser.Func_control_stmContext):
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        return self.visit(ctx.block_stm())

    # var_stm: variables ignore
    def visitVar_stm(self, ctx: ZCodeParser.Var_stmContext):
        return self.visit(ctx.variables())

    # func_stm: ID CLB expr_list? CRB ignore
    def visitFunc_stm(self, ctx: ZCodeParser.Func_stmContext):
        if ctx.expr_list():
            return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))
        return CallStmt(Id(ctx.ID().getText()), [])

    # asg_stm: ID (SLB expr_list SRB)? ASG expression ignore
    def visitAsg_stm(self, ctx: ZCodeParser.Asg_stmContext):
        if ctx.expr_list():
            return Assign(
                ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.expr_list())),
                self.visit(ctx.expression()),
            )
        return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression()))

    # if_stm: IF CLB expression CRB ignore? statement elif_stm (ELSE statement)? ignore?;
    def visitIf_stm(self, ctx: ZCodeParser.If_stmContext):
        if ctx.ELSE():
            return If(
                self.visit(ctx.expression()),
                self.visit(ctx.statement()[0]),
                self.visit(ctx.elif_stm()),
                self.visit(ctx.statement()[1]),
            )

        return If(
            self.visit(ctx.expression()),
            self.visit(ctx.statement()[0]),
            self.visit(ctx.elif_stm()),
            None,
        )

    # elif_stm: ELIF CLB expression CRB ignore? statement elif_stm | ;
    def visitElif_stm(self, ctx: ZCodeParser.Elif_stmContext):
        if ctx.elif_stm():
            return [
                (self.visit(ctx.expression()), self.visit(ctx.statement()))
            ] + self.visit(ctx.elif_stm())
        return []

    # for_stm: FOR ID UNTIL expression BY expression ignore? statement ignore?
    def visitFor_stm(self, ctx: ZCodeParser.For_stmContext):
        return For(
            Id(ctx.ID().getText()),
            self.visit(ctx.expression()[0]),
            self.visit(ctx.expression()[1]),
            self.visit(ctx.statement()),
        )

    # break_stm: BREAK ignore
    def visitBreak_stm(self, ctx: ZCodeParser.Break_stmContext):
        return Break()

    # continue_stm: CONTINUE ignore
    def visitContinue_stm(self, ctx: ZCodeParser.Continue_stmContext):
        return Continue()

    # return_stm: RETURN expression? ignore
    def visitReturn_stm(self, ctx: ZCodeParser.Return_stmContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return()

    # block_stm: BEGIN ignore stm_list END ignore
    def visitBlock_stm(self, ctx: ZCodeParser.Block_stmContext):
        if ctx.stm_list():
            return Block(self.visit(ctx.stm_list()))
        return Block([])

    # expr_list: expression COMMA expr_list | expression
    def visitExpr_list(self, ctx: ZCodeParser.Expr_listContext):
        if ctx.expr_list():
            return [self.visit(ctx.expression())] + self.visit(ctx.expr_list())
        return [self.visit(ctx.expression())]

    # expression: expression1 CONCAT expression1 | expression1
    def visitExpression(self, ctx: ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1()[0])
        operation = ctx.CONCAT().getText()
        left = self.visit(ctx.expression1()[0])
        right = self.visit(ctx.expression1()[1])
        return BinaryOp(operation, left, right)

    # expression1: expression2 (RES | EQL | UEQL | GT | GTE | LT | LTE) expression2 | expression2;
    def visitExpression1(self, ctx: ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2()[0])
        if ctx.RES():
            operation = ctx.RES().getText()
        elif ctx.EQL():
            operation = ctx.EQL().getText()
        elif ctx.UEQL():
            operation = ctx.UEQL().getText()
        elif ctx.GT():
            operation = ctx.GT().getText()
        elif ctx.GTE():
            operation = ctx.GTE().getText()
        elif ctx.LT():
            operation = ctx.LT().getText()
        elif ctx.LTE():
            operation = ctx.LTE().getText()
        left = self.visit(ctx.expression2()[0])
        right = self.visit(ctx.expression2()[1])
        return BinaryOp(operation, left, right)

    # expression2: expression2 (AND | OR) expression3 | expression3
    def visitExpression2(self, ctx: ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        if ctx.AND():
            operation = ctx.AND().getText()
        elif ctx.OR():
            operation = ctx.OR().getText()
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(operation, left, right)

    # expression3: expression3 (ADD | SUB) expression4 | expression4
    def visitExpression3(self, ctx: ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        if ctx.ADD():
            operation = ctx.ADD().getText()
        elif ctx.SUB():
            operation = ctx.SUB().getText()
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(operation, left, right)

    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5
    def visitExpression4(self, ctx: ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        if ctx.MUL():
            operation = ctx.MUL().getText()
        elif ctx.DIV():
            operation = ctx.DIV().getText()
        elif ctx.MOD():
            operation = ctx.MOD().getText()
        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(operation, left, right)

    # expression5: NOT expression5 | expression6
    def visitExpression5(self, ctx: ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        operation = ctx.NOT().getText()
        expr = self.visit(ctx.expression5())
        return UnaryOp(operation, expr)

    # expression6: (ADD | SUB) expression6 | expression7
    def visitExpression6(self, ctx: ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        if ctx.ADD():
            operation = ctx.ADD().getText()
        elif ctx.SUB():
            operation = ctx.SUB().getText()
        expr = self.visit(ctx.expression6())
        return UnaryOp(operation, expr)

    # expression7: (ID | ID CLB index_operators? CRB) SLB index_operators SRB | expression8
    def visitExpression7(self, ctx: ZCodeParser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(
                Id(ctx.ID().getText()), self.visit(ctx.index_operators()[0])
            )
        elif len(ctx.index_operators()) == 2:
            return ArrayCell(
                CallExpr(Id(ctx.ID().getText()), self.visit(ctx.index_operators()[0])),
                self.visit(ctx.index_operators()[1]),
            )
        return ArrayCell(
            CallExpr(Id(ctx.ID().getText()), []), self.visit(ctx.index_operators()[0])
        )

    # expression8: ID | typ | sub_expr | func_call
    def visitExpression8(self, ctx: ZCodeParser.Expression8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.typ():
            return self.visit(ctx.typ())
        elif ctx.sub_expr():
            return self.visit(ctx.sub_expr())
        return self.visit(ctx.func_call())

    # sub_expr: CLB expression CRB
    def visitSub_expr(self, ctx: ZCodeParser.Sub_exprContext):
        return self.visit(ctx.expression())

    # func_call: ID CLB expr_list? CRB;
    def visitFunc_call(self, ctx: ZCodeParser.Func_callContext):
        if ctx.expr_list():
            return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))
        return CallExpr(Id(ctx.ID().getText()), [])

    # index_operators : expression | expression COMMA index_operators;
    def visitIndex_operators(self, ctx: ZCodeParser.Index_operatorsContext):
        if ctx.index_operators():
            return [self.visit(ctx.expression())] + self.visit(ctx.index_operators())
        return [self.visit(ctx.expression())]

    # typ: NUM_LIT | BOOL_LIT | STR_LIT | arr_lit
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUM_LIT():
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif ctx.BOOL_LIT():
            bool_value = ctx.BOOL_LIT().getText() == "true"
            return BooleanLiteral(bool_value)
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        elif ctx.arr_lit():
            return self.visit(ctx.arr_lit())

    # normal_typ_name: NUMBER | BOOL | STRING
    def visitNormal_typ_name(self, ctx: ZCodeParser.Normal_typ_nameContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()

    # arr_lit: SLB expr_list SRB;
    def visitArr_lit(self, ctx: ZCodeParser.Arr_litContext):
        return ArrayLiteral(self.visit(ctx.expr_list()))

    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx: ZCodeParser.IgnoreContext):
        return None
