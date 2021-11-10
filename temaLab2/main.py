import AFD
import utils

cod_atom = utils.cod_atom
fip = []
ts = []
index = 0

accoladeCnt = 0
roundBracketCnt = 0

muchii, stari_initiale, stari_finale = utils.read_file("constante.txt")
afdConstante = AFD.AFD()
afdConstante.reInit(muchii, stari_initiale, stari_finale)

muchii, stari_initiale, stari_finale = utils.read_file("identificatori.txt")
afdIdentificatori = AFD.AFD()
afdIdentificatori.reInit(muchii, stari_initiale, stari_finale)

def check_include_statement(l, i):
    errors = ""
    elements = l.split()
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: '#include \"library\"'\n"
        return errors
    if element != '#include':
        errors += "Err at line " + str(i) + ": first word should be '#include'\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: '#include \"library\"'\n"
        return errors
    if element not in utils.libraries:
        errors += "Err at line " + str(i) + ": library not found\n"
    if len(elements) > 0:
        errors += "Err at line " + str(i) + ": not a valid include statement. Too many atoms\n"

    return errors


def check_using_statement(l, i):
    errors = ""
    elements = l.split()
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'using namespace std;'\n"
        return errors
    if element != 'using':
        errors += "Err at line " + str(i) + ": first word should be 'using'\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'using namespace std;'\n"
        return errors
    if element != 'namespace':
        errors += "Err at line " + str(i) + ": missing word 'namespace'\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'using namespace std;'\n"
        return errors
    if element != 'std':
        errors += "Err at line " + str(i) + ": missing word 'std'\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'using namespace std;'\n"
        return errors
    if element != ';':
        errors += "Err at line " + str(i) + ": missing ';'\n"
    if len(elements) > 0:
        errors += "Err at line " + str(i) + ": not a valid using statement. Too many atoms\n"

    return errors


def check_main_line(l, i):
    errors = ""
    elements = l.split()
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'int main ( ) { " \
                                            "'instructions' }\n "
        return errors
    if element != 'int':
        errors += "Err at line " + str(i) + ": first word should be 'int'\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'int main ( ) { " \
                                            "'instructions' }\n "
        return errors
    if element != 'main':
        errors += "Err at line " + str(i) + ": second word should be 'main'\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'int main ( ) { " \
                                            "\"instructions\" }'\n "
        return errors
    if element != '(':
        errors += "Err at line " + str(i) + ": third atom should be '('\n"
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing words. Accepted using statement: 'int main ( ) { " \
                                            "\"instructions\" }'\n "
        return errors
    if element != ')':
        errors += "Err at line " + str(i) + ": forth atom should be ')'\n"
    if len(elements) > 0:
        errors += "Err at line " + str(i) + ": not a valid main statement. Too many atoms\n"

    return errors


def check_accolade(l, i):
    global accoladeCnt
    errors = ""
    elements = l.split()
    if len(elements) > 0:
        element = elements.pop(0)
    else:
        errors += "Err at line " + str(i) + ": missing required {\n"
        return errors
    if element != '{':
        errors += "Err at line " + str(i) + ": you should insert '{'\n"
    else:
        accoladeCnt += 1
    if len(elements) > 0:
        errors += "Err at line " + str(i) + ": not a valid main statement. Too many atoms\n"
    return errors


def validate_lines(lines):
    global accoladeCnt
    global roundBracketCnt
    errors = ""
    for i in range(len(lines)):

        elements = lines[i].split()

        if '#include' == elements[0]:
            errors += check_include_statement(lines[i], i)
            i += 1
            continue
        if 'using' == elements[0]:
            errors += check_using_statement(lines[i], i)
            i += 1
            continue
        if 'main' in elements:
            errors += check_main_line(lines[i], i)
            i += 1
            errors += check_accolade(lines[i], i)
            i += 1

            continue
    return errors


def check_TS(el):
    for element in ts:
        if element[0] == el:
            return element[1]
    return -1


def add_ts(el, poz):
    global ts

    if len(ts) == 0:
        ts.append((el, poz))
        return
    if el > ts[-1][0]:
        ts.append((el, poz))
        return
    cnt = 0
    while el > ts[cnt][0]:
        cnt += 1
    ts = ts[:cnt] + [(el, poz)] + ts[cnt:]


def add_in_ts(el):
    global index
    pos = check_TS(el)
    if pos == -1:
        add_ts(el, index)
        index += 1
        return index - 1
    else:
        return pos


def add_in_tables(l, i):
    global index
    err = ""
    elements = l.split()
    for el in elements:
        if el in cod_atom:
            fip.append((cod_atom[el], '-'))
        elif utils.check_constant(el, afdConstante):
            indx = add_in_ts(el)
            fip.append((cod_atom['CONST'], indx))
        elif utils.check_variable(el, afdIdentificatori):
            indx = add_in_ts(el)
            fip.append((cod_atom['ID'], indx))
        else:
            err += "Err at line " + str(i) + ": not a valid ID atom, it should be no longer than 255 chars and it " \
                                             "must contain only lowercase letters\n "
    return err


def print_tables():
    with open("myfile.txt", "w") as f:
        f.writelines('FIP\n')
        for el in fip:
            f.writelines(str(el) + '\n')
        f.writelines('\nTS\n')

        for el in ts:
            f.writelines(str(el) + '\n')


def main():

    with open('date.txt') as f:
        lines = f.readlines()
        err = ""
        i = 0
        for l in lines:
            l = l.strip()
            err += add_in_tables(l, i)
            i = i + 1
        err += validate_lines(lines)
        print(err)
    print_tables()


main()
