# import re
#
# class AssignmentError(Exception): pass
#
# a, b = re.compile(r'[A-Za-z0-9_]+'), re.compile(r'[^+\-*/%( ]\(')
#
# def expr_check(s, ids):
#     objs = re.findall(a, s)
#     if "//" in s or "**" in s or len(re.findall(b, s)) or "." in s:
#         raise SyntaxError
#     for obj in objs:
#         if obj in ids and obj.isidentifier():
#             s = s.replace(obj, ids[obj])
#         elif obj.isidentifier():
#             raise NameError
#         elif not obj.isdigit():
#             raise SyntaxError
#     s = s.replace("/", "//")
#     return eval(s)
#
#
# def line_check(s, ids):
#     if s.startswith("#"):
#         return ids
#     elif "=" in s:
#         if s.count("=") > 1:
#             raise SyntaxError
#         id, expr = s.split("=")
#         id, expr = id.strip(), expr.strip()
#         if not id.isidentifier():
#             raise AssignmentError
#         assignment = expr_check(expr, ids)
#         ids[id] = str(assignment)
#         return ids
#     else:
#         print(expr_check(s, ids))
#         return ids
#
# ids = {}
# while s := input():
#     try:
#         ids = line_check(s, ids)
#     except NameError:
#         print("Name error")
#     except SyntaxError:
#         print("Syntax error")
#     except AssignmentError:
#         print("Assignment error")
#     except Exception:
#         print("Runtime error")

import re

class AssignmentError(Exception): pass


def expr_check(s, ids):
    if "**" in s or "//" in s:
        raise SyntaxError
    if re.findall(r'[a-zA-z]\(', s):
        raise SyntaxError
    ops = re.sub("/", "//", re.sub(r'[+\-*/%()]', lambda c: " " + c.group(0) + " ", re.sub(" ", "", s))).split()
    for idx, op in enumerate(ops):
        if op.isidentifier():
            ops[idx] = "_C_" + op
            if ops[idx] not in ids:
                raise NameError
        elif not op.isdigit() and op not in "+-*//%()":
            raise SyntaxError
    return eval("".join(ops), {}, ids)

def line_check(s, ids):
    if s.startswith("#"):
        return ids
    elif "=" in s:
        assignment, *expr = s.split("=")
        if len(expr) > 1:
            raise SyntaxError
        assignment, expr = assignment.strip(), expr[0].strip()
        if not assignment.isidentifier():
            raise AssignmentError
        value = expr_check(expr, ids)
        ids["_C_" + assignment] = value
        return ids
    else:
        print(expr_check(s, ids))
        return ids

ids = {}

while s:= input():
    try:
        ids = line_check(s, ids)
    except NameError:
        print("Name error")
    except SyntaxError:
        print("Syntax error")
    except AssignmentError:
        print("Assignment error")
    except Exception:
        print("Runtime error")

