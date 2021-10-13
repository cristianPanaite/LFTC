reservedWords = ['#include', 'if', 'else', 'while', 'cout', 'cin']
libraries = ['<iostream>']
dataType = ['int', 'double']
arithmeticOperators = ['+', '-', '/', '*', '<<', '>>', '=']
logicOperator = ['||', '&&', '<=', '<', '>', '>=', '==', '!=']


def main():
    with open('date.txt') as f:
        lines = f.readlines()
        for l in lines:
            elements = l.split()
            for e in elements:
                if ';' in e:
                    newElement = e.replace(';', '')
                    print(newElement)
                    print(';')
                else:
                    print(e)


main()
