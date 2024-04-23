from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Zcode:
    pass


class FuncZcode(Zcode):
    def __init__(self, param=[], typ=None, body=False):
        self.param = param
        self.typ = typ
        self.body = body


class VarZcode(Zcode):
    def __init__(self, typ=None):
        self.typ = typ


class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType


class StaticChecker(BaseVisitor, Utils):
    def __init__(
        self,
        ast,
    ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = [
            {
                "readNumber": FuncZcode([], NumberType(), True),
                "readBool": FuncZcode([], BoolType(), True),
                "readString": FuncZcode([], StringType(), True),
                "writeNumber": FuncZcode([NumberType()], VoidType(), True),
                "writeBool": FuncZcode([BoolType()], VoidType(), True),
                "writeString": FuncZcode([StringType()], VoidType(), True),
            }
        ]

    def check(self):
        self.visit(self.ast, [{}])
        return None

    def comparType(self, lhs, rhs):
        if type(lhs) != type(rhs):
            return False
        elif isinstance(lhs, ArrayType):
            if len(lhs.size) != len(rhs.size) or type(lhs.eleType) != type(rhs.eleType):
                return False
            for i in range(len(lhs.size)):
                if lhs.size[i] != rhs.size[i]:
                    return False
        return True

    def comparListType(self, listLHS, listRHS):
        if len(listLHS) != len(listRHS):
            return False
        for i in range(0, len(listLHS)):
            if not self.comparType(listLHS[i], listRHS[i]):
                return False
        return True

    def setTypeArray(self, typeArray, typeArrayZcode):
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        if len(typeArray.size) == 1:
            for i, zcode_element in enumerate(typeArrayZcode.eleType):
                if isinstance(zcode_element, Zcode):
                    zcode_element.typ = typeArray.eleType
                else:
                    return False
        else:
            for i, zcode_element in enumerate(typeArrayZcode.eleType):
                if isinstance(zcode_element, Zcode):
                    zcode_element.typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif isinstance(zcode_element, ArrayZcode):
                    if not self.setTypeArray(
                        ArrayType(typeArray.size[1:], typeArray.eleType), zcode_element
                    ):
                        return False
                else:
                    return False
        return True

    def inferBinaryOperationType(self, lhs, rhs, expected_type, result_type, ast):
        if self.comparType(lhs, expected_type) and self.comparType(rhs, expected_type):
            return result_type
        elif self.comparType(lhs, expected_type) and isinstance(rhs, Zcode):
            rhs.typ = expected_type
            return result_type
        elif isinstance(lhs, Zcode) and self.comparType(rhs, expected_type):
            lhs.typ = expected_type
            return result_type
        elif isinstance(lhs, Zcode) and isinstance(rhs, Zcode):
            lhs.typ = expected_type
            rhs.typ = expected_type
            return result_type
        else:
            raise TypeMismatchInExpression(ast)

    def visitProgram(self, ast, param):
        for declaration in ast.decl:
            self.visit(declaration, param)
        for function_dict in self.listFunction:
            for name, func in function_dict.items():
                if not func.body:
                    raise NoDefinition(name)
        main_func = None
        for function_dict in self.listFunction:
            main_func = function_dict.get("main")
            if main_func:
                break
        if main_func is None:
            raise NoEntryPoint()
        if len(main_func.param) != 0:
            raise NoEntryPoint()
        if not self.comparType(main_func.typ, VoidType()):
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        var_name = ast.name.name
        if isinstance(param, list):
            if var_name in param[0]:
                raise Redeclared("Variable", var_name)
            param[0][var_name] = VarZcode(ast.varType)
        elif isinstance(param, dict):
            if var_name in param:
                raise Redeclared("Parameter", var_name)
            param[var_name] = VarZcode(ast.varType)
        if ast.varInit:
            lhs = ast.varType if ast.varType else param[0][ast.name.name]
            rhs = self.visit(ast.varInit, param)
            if isinstance(lhs, Zcode) and isinstance(rhs, Zcode):
                raise TypeCannotBeInferred(ast)
            elif isinstance(lhs, Zcode) and isinstance(rhs, ArrayZcode):
                raise TypeCannotBeInferred(ast)
            elif not isinstance(lhs, Zcode) and isinstance(rhs, ArrayZcode):
                if isinstance(lhs, (StringType, BoolType, NumberType)):
                    raise TypeMismatchInStatement(ast)
                elif isinstance(lhs, ArrayType):
                    if not self.setTypeArray(lhs, rhs):
                        raise TypeMismatchInStatement(ast)
            elif isinstance(lhs, Zcode) and isinstance(
                rhs, (StringType, BoolType, NumberType, ArrayType)
            ):
                lhs.typ = rhs
            elif isinstance(
                lhs, (StringType, BoolType, NumberType, ArrayType)
            ) and isinstance(rhs, Zcode):
                rhs.typ = lhs
            elif isinstance(
                lhs, (StringType, BoolType, NumberType, ArrayType)
            ) and isinstance(rhs, (StringType, BoolType, NumberType, ArrayType)):
                if not self.comparType(lhs, rhs):
                    raise TypeMismatchInStatement(ast)

    def visitFuncDecl(self, ast, param):
        func_name = ast.name.name
        func_exists = self.listFunction[0].get(func_name)
        if func_exists and not (func_exists.body == False and ast.body):
            raise Redeclared("Function", func_name)
        listParam = {}
        typeParam = []
        for i in ast.param:
            self.visit(i, listParam)
            typeParam.append(i.varType)
        self.Return = False
        isFuncDeclaration = False
        if func_exists and not func_exists.body and ast.body:
            lhs = func_exists.param
            rhs = typeParam
            if not self.comparListType(lhs, rhs):
                raise Redeclared("Function", func_name)
            func_exists.body = True
            self.function = self.listFunction[0][func_name]
            self.visit(ast.body, [listParam] + param)
        elif ast.body is None:
            isFuncDeclaration = True
            self.listFunction[0][func_name] = FuncZcode(typeParam, None, False)
        elif ast.body is not None:
            self.listFunction[0][func_name] = FuncZcode(typeParam, None, True)
            self.function = self.listFunction[0][func_name]
            self.visit(ast.body, [listParam] + param)
        if not isFuncDeclaration:
            if not self.Return:
                func_typ = self.listFunction[0][ast.name.name].typ
                if func_typ is None:
                    self.listFunction[0][ast.name.name].typ = VoidType()
                elif not self.comparType(func_typ, VoidType()):
                    raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast, param):
        for id_name in param:
            if id_name.get(ast.name):
                if id_name.get(ast.name).typ:
                    return id_name.get(ast.name).typ
                elif not id_name.get(ast.name).typ:
                    return id_name.get(ast.name)
        raise Undeclared("Identifier", ast.name)

    def visitCallExpr(self, ast, param):
        expr_name = ast.name.name
        if expr_name not in self.listFunction[0]:
            raise Undeclared("Function", expr_name)
        param_list = self.listFunction[0][expr_name].param
        arg_list = ast.args
        if len(param_list) != len(arg_list):
            raise TypeMismatchInExpression(ast)
        for param, arg in zip(param_list, arg_list):
            param_type = self.visit(param, param)
            arg_type = self.visit(arg, param)
            if isinstance(arg_type, Zcode):
                arg_type.typ = param_type
            else:
                if not self.comparType(param_type, arg_type):
                    raise TypeMismatchInExpression(ast)
        function = self.listFunction[0][expr_name]
        if function.typ is None:
            return function
        elif self.comparType(function.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        else:
            return function.typ

    def visitCallStmt(self, ast, param):
        stmt_name = ast.name.name
        if stmt_name not in self.listFunction[0]:
            raise Undeclared("Function", stmt_name)
        param_list = self.listFunction[0][stmt_name].param
        arg_list = ast.args
        if len(param_list) != len(arg_list):
            raise TypeMismatchInStatement(ast)
        for param, arg in zip(param_list, arg_list):
            param_type = self.visit(param, param)
            arg_type = self.visit(arg, param)
            if isinstance(arg_type, Zcode):
                arg_type.typ = param_type
            else:
                if not self.comparType(param_type, arg_type):
                    raise TypeMismatchInStatement(ast)
        function = self.listFunction[0][stmt_name]
        if function.typ is None:
            return function
        elif not self.comparType(function.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        else:
            return function.typ

    def visitIf(self, ast, param):
        expr_type = self.visit(ast.expr, param)
        if isinstance(expr_type, Zcode):
            expr_type.typ = BoolType()
        elif not self.comparType(expr_type, BoolType()):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, [{}] + param)
        for elif_clause in ast.elifStmt:
            expr_type = self.visit(elif_clause[0], param)
            if isinstance(expr_type, Zcode):
                expr_type.typ = BoolType()
            elif not self.comparType(expr_type, BoolType()):
                raise TypeMismatchInStatement(ast)
            self.visit(elif_clause[1], [{}] + param)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)

    def visitFor(self, ast, param):
        name_type = self.visit(ast.name, param)
        cond_expr_type = self.visit(ast.condExpr, param)
        upd_expr_type = self.visit(ast.updExpr, param)
        if isinstance(name_type, Zcode):
            name_type.typ = NumberType()
        elif not self.comparType(NumberType(), name_type):
            raise TypeMismatchInStatement(ast)
        if isinstance(cond_expr_type, Zcode):
            cond_expr_type.typ = BoolType()
        elif not self.comparType(BoolType(), cond_expr_type):
            raise TypeMismatchInStatement(ast)
        if isinstance(upd_expr_type, Zcode):
            upd_expr_type.typ = NumberType()
        elif not self.comparType(NumberType(), upd_expr_type):
            raise TypeMismatchInStatement(ast)
        self.BlockFor = self.BlockFor + 1
        self.visit(ast.body, [{}] + param)
        self.BlockFor = self.BlockFor - 1

    def visitReturn(self, ast, param):
        self.Return = True
        if self.function.typ is not None:
            lhs = self.function.typ
        else:
            lhs = self.function
        if ast.expr:
            rhs = self.visit(ast.expr, param)
        else:
            rhs = VoidType()
        if isinstance(lhs, Zcode) and isinstance(rhs, Zcode):
            raise TypeCannotBeInferred(stmt=ast)
        elif not isinstance(lhs, Zcode) and isinstance(rhs, Zcode):
            rhs.typ = lhs
        elif isinstance(lhs, Zcode) and not isinstance(rhs, Zcode):
            lhs.typ = rhs
        elif not self.comparType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        if (
            param[0].get(ast.lhs.name).typ != lhs
            and param[0].get(ast.lhs.name).typ is not None
        ):
            lhs = param[0].get(ast.lhs.name).typ
        if isinstance(lhs, Zcode) and isinstance(rhs, Zcode):
            raise TypeCannotBeInferred(stmt=ast)
        elif not isinstance(lhs, Zcode) and isinstance(rhs, Zcode):
            rhs.typ = lhs
        elif isinstance(lhs, Zcode) and not isinstance(rhs, Zcode):
            lhs.typ = rhs
        elif not self.comparType(lhs, rhs):
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast, param):
        lhs = self.visit(ast.left, param)
        rhs = self.visit(ast.right, param)
        operation = ast.op

        if operation in ["+", "-", "*", "/", "%"]:
            return self.inferBinaryOperationType(
                lhs, rhs, NumberType(), NumberType(), ast
            )
        elif operation in ["and", "or"]:
            return self.inferBinaryOperationType(lhs, rhs, BoolType(), BoolType(), ast)
        elif operation in ["=", "!=", "<", ">", ">=", "<="]:
            return self.inferBinaryOperationType(
                lhs, rhs, NumberType(), BoolType(), ast
            )
        elif operation in ["=="]:
            return self.inferBinaryOperationType(
                lhs, rhs, StringType(), BoolType(), ast
            )
        elif operation in ["..."]:
            return self.inferBinaryOperationType(
                lhs, rhs, StringType(), StringType(), ast
            )
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, param):
        unary_expr = self.visit(ast.operand, param)
        operation = ast.op
        if operation in ["not"]:
            if self.comparType(unary_expr, BoolType()):
                return BoolType()
            elif isinstance(unary_expr, Zcode):
                unary_expr.typ = BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif operation in ["+", "-"]:
            if self.comparType(unary_expr, NumberType()):
                return NumberType()
            elif isinstance(unary_expr, Zcode):
                unary_expr.typ = NumberType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast, param):
        array_cell = self.visit(ast.arr, param)
        if not isinstance(array_cell, ArrayType):
            raise TypeMismatchInExpression(ast)
        for idx in ast.idx:
            rhs = self.visit(idx, param)
            if isinstance(rhs, Zcode):
                rhs.typ = NumberType()
            elif not self.comparType(rhs, NumberType()):
                raise TypeMismatchInExpression(ast)
        if len(array_cell.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(array_cell.size) == len(ast.idx):
            return array_cell.eleType
        else:
            new_size = array_cell.size[len(ast.idx) :]
            return ArrayType(new_size, array_cell.eleType)

    def visitArrayLiteral(self, ast, param):
        for item in ast.value:
            self.visit(item, param)
        typ = self.visit(ast.value[0], param)

        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)

    def visitBlock(self, ast, param):
        for item in ast.stmt:
            if type(item) is Block:
                self.visit(item, [{}] + param)
            else:
                self.visit(item, param)

    def visitContinue(self, ast, param):
        if self.BlockFor == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.BlockFor == 0:
            raise MustInLoop(ast)

    def visitNumberType(self, ast, param):
        return ast

    def visitBoolType(self, ast, param):
        return ast

    def visitStringType(self, ast, param):
        return ast

    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, ast.eleType)

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()
