import argparse
import ast
from translate import tr
from typechecking.prog_ast import *


def impliciteSide_effect_checking_err(fun_def, ctx, global_vars):
    for instr in fun_def.body:
        # check if instruction is assign
        if isinstance(instr, Assign):
            target = instr.target

            # checking for vars
            if isinstance(target, LHSVar):
                side_effect_checking_target_err(target, global_vars, ctx)
            # checking for tuples
            elif isinstance(target, LHSTuple):
                side_effect_checking_target_err(target, global_vars, ctx)

        # check if instruction is ContainerAssign
        elif isinstance(instr, ContainerAssign):
            side_effect_checking_target_err(
                instr.container_expr.name, global_vars, ctx)

        # ecall chacking
        elif isinstance(instr, ECall):
            fun_name = instr.fun_name
            if fun_name == "append" or fun_name == "remove" or fun_name == "add" or "write":
                side_effect_checking_target_err(
                    instr.receiver.name, global_vars, ctx)


# check if target of assign is in global variables
def side_effect_checking_target_err(target, global_vars, ctx):
    for v in global_vars:
        if str(target) == str(v.target):
            ctx.add_type_error(implicitEffectCheckingError(target))


class implicitEffectCheckingError(TypeError):
    def __init__(self, node):
        self.node = node

    def is_fatal(self):
        return False

    def fail_string(self):
        return "ImplicitEffectCheckingError[{}]@{}:{}".format(str(self.node.ast.__class__.__name__), self.node.ast.lineno, self.node.ast.col_offset)

    def report(self, report):
        report.add_convention_error('error', tr('side effect'), self.node.ast.lineno, self.node.ast.col_offset, tr(
            "The variable '{}' is a global variable, you can't write on it.").format(str(self.node)))


if __name__ == '__main__':
    import argparse
    import astpp
    from astpp import *
    arg_parser = argparse.ArgumentParser(description='')
    arg_parser.add_argument('file')

    args = arg_parser.parse_args()

    if args.file is not None:
        program = Program()
        program.build_from_file(args.file)
        print('Global Variables list :')
        for gvar in program.global_vars:
            print(str(gvar.target))
        for func_name, func_def in program.functions.items():
            impliciteSide_effect_checking_err(
                func_def, program.global_vars, ctx)

    else:
        print("Input file missing")
