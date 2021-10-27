"""
BNF tip input
<input>:= <nr_tranzitii>
          <tranzitie> {<nr_tranzitii>}
          <nr_intrari>
          <intrari> {<nr_intrari>}
          <nr_finale>
          <finale> {<nr_finale>}
<nr_tranzitii> := [1-9][0-9]*
<nr_intrari> := [1-9][0-9]*
<nr_finale> := [1-9][0-9]*
<tranzitie> := <stare> <stare> <element>
<element> := [0 - 9] | '-'
<intrari> := <stare>
 <finale> := <stare>
 <stare> := 'q0' | 'q'[1-9][0-9]*
"""
import AFD


def read_file():
    with open("date.txt") as f:
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


def read_cmd():
    nr_tranzitii = int(input("Nr tranzitii: ").strip())
    muchii = []
    while nr_tranzitii:
        tranzitie = input("Tranzitie {}".format(nr_tranzitii)).strip().split()
        muchii.append((tranzitie[0], tranzitie[1], tranzitie[2]))
        nr_tranzitii -= 1
    nr_intrari = int(input("Nr stari initiale: ").strip())
    stari_initiale = []
    while nr_intrari:
        stare = input("Stare initiala {}: ".format(nr_intrari).strip())
        stari_initiale.append(stare)
        nr_intrari -= 1
    nr_finale = int(input("Nr stari finale: ").strip())
    stari_finale = []
    while nr_finale:
        stari_finale.append(input("Stare finala {}: ".format(nr_finale)).strip())
        nr_finale -= 1
    return [muchii, stari_initiale, stari_finale]


def print_options():
    print("Optiuni:")
    print("\t1. Citeste AFD din fisier")
    print("\t2. Citeste AFD de la tastatura")
    print("\t3. Afiseaza multimea starilor")
    print("\t4. Afiseaza alfabetul")
    print("\t5. Afiseaza tranzitiile")
    print("\t6. Afiseaza multimea starilor finale")
    print("\t7. Verifica secventa")
    print("\t8. Determina cel mai lung prefix")
    print("\t0. exit")
    print("Insereaza numarul corespunzator optiunii dorite")


def main():
    AutomatFinitDeterminist = AFD.AFD()
    while True:
        print("AFD program")
        print_options()
        cmd = int(input(">>>"))
        if cmd == 1:
            muchii, stari_initiale, stari_finale = read_file()
            AutomatFinitDeterminist.reInit(muchii, stari_initiale, stari_finale)
            continue
        if cmd == 2:
            muchii, stari_initiale, stari_finale = read_cmd()
            AutomatFinitDeterminist.reInit(muchii, stari_initiale, stari_finale)
            continue
        if cmd == 3:
            print(AutomatFinitDeterminist.get_multimea_starilor())
            continue
        if cmd == 4:
            print(AutomatFinitDeterminist.get_alfabet())
            continue
        if cmd == 5:
            tranzitii = AutomatFinitDeterminist.get_tranzitii()
            for t in tranzitii:
                print(t)
            continue
        if cmd == 6:
            print(AutomatFinitDeterminist.get_stari_finale())
            continue
        if cmd == 7:
            secventa = input("Introdu secventa: ")
            print(AutomatFinitDeterminist.accepta(secventa))
            continue
        if cmd == 8:
            secventa = input("Introdu secventa: ")
            print(AutomatFinitDeterminist.prefix_maxim(secventa))
            continue
        if cmd == 0:
            break


main()
