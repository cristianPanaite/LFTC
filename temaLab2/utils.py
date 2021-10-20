import re

cod_atom = {
    'ID': 0,
    'CONST': 1,
    '#include': 2,
    'using': 3,
    'namespace': 4,
    'std': 5,
    ';': 6,
    'int': 7,
    'main': 8,
    '(': 9,
    ')': 10,
    '{': 11,
    '}': 12,
    '<iostream>': 13,
    'struct': 14,
    'double': 15,
    '=': 16,
    '/': 17,
    '*': 18,
    '+': 19,
    '-': 20,
    'if': 21,
    'else': 22,
    '||': 23,
    '&&': 24,
    '>': 25,
    '<': 26,
    '>=': 27,
    '<=': 28,
    '==': 29,
    '!=': 30,
    'while': 31,
    'cin': 32,
    'cout': 33,
    '<<': 34,
    '>>': 35
}

libraries = ['<iostream>']


def check_constant(value):
    try:
        x = float(value)
        return True
    except:
        return False


def check_variable(value):
    if len(value) > 250 or len(value) < 1:
        return False
    for i in value:
        if i < 'a' or i > 'z':
            return False
    return True
