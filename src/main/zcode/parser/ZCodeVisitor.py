# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#program_stm.
    def visitProgram_stm(self, ctx:ZCodeParser.Program_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare_stm.
    def visitDeclare_stm(self, ctx:ZCodeParser.Declare_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normal_var.
    def visitNormal_var(self, ctx:ZCodeParser.Normal_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_var.
    def visitDynamic_var(self, ctx:ZCodeParser.Dynamic_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#num_list.
    def visitNum_list(self, ctx:ZCodeParser.Num_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stm_list.
    def visitStm_list(self, ctx:ZCodeParser.Stm_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare_part_stm.
    def visitDeclare_part_stm(self, ctx:ZCodeParser.Declare_part_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#flow_control_stm.
    def visitFlow_control_stm(self, ctx:ZCodeParser.Flow_control_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_control_stm.
    def visitFunc_control_stm(self, ctx:ZCodeParser.Func_control_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_stm.
    def visitVar_stm(self, ctx:ZCodeParser.Var_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_stm.
    def visitFunc_stm(self, ctx:ZCodeParser.Func_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#asg_stm.
    def visitAsg_stm(self, ctx:ZCodeParser.Asg_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stm.
    def visitIf_stm(self, ctx:ZCodeParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stm.
    def visitElif_stm(self, ctx:ZCodeParser.Elif_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stm.
    def visitFor_stm(self, ctx:ZCodeParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stm.
    def visitBreak_stm(self, ctx:ZCodeParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stm.
    def visitContinue_stm(self, ctx:ZCodeParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stm.
    def visitReturn_stm(self, ctx:ZCodeParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stm.
    def visitBlock_stm(self, ctx:ZCodeParser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression8.
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sub_expr.
    def visitSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normal_typ_name.
    def visitNormal_typ_name(self, ctx:ZCodeParser.Normal_typ_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_lit.
    def visitArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)



del ZCodeParser