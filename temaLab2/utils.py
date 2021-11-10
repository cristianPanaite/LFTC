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


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        nr_tranzitii = lines.pop(0)
        nr_tranzitii = nr_tranzitii.strip()
        nr_tranzitii = int(nr_tranzitii)
        muchii = []
        while nr_tranzitii:
            tranzitie = lines.pop(0).strip().split()
            muchii.append((tranzitie[0], tranzitie[1], tranzitie[2]))
            nr_tranzitii -= 1
        nr_intrari = int(lines.pop(0).strip())
        stari_initiale = []
        while nr_intrari:
            stare = lines.pop(0).strip()
            stari_initiale.append(stare)
            nr_intrari -= 1
        nr_finale = int(lines.pop(0).strip())
        stari_finale = []
        while nr_finale:
            stari_finale.append(lines.pop(0).strip())
            nr_finale -= 1
    return [muchii, stari_initiale, stari_finale]


def check_constant(value, afd):
    return afd.accepta(value)


def check_variable(value, afd):
    return afd.accepta(value)
