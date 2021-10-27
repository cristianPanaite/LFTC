def parcurgere(graf, stare_curenta, secventa, pos_secventa):
    if pos_secventa == len(secventa):
        return len(secventa)
    if stare_curenta not in graf:
        return pos_secventa
    lenMax = pos_secventa
    for muchie in graf[stare_curenta]:
        if muchie.value == secventa[pos_secventa]:
            length = parcurgere(graf, muchie.destination, secventa, pos_secventa + 1)
            if length > lenMax:
                lenMax = length
    return lenMax


def parcurgere_accepta(graf, stare_curenta, secventa, pos_secventa, stari_finale):
    if pos_secventa == len(secventa):
        if stare_curenta in stari_finale:
            return True
        else:
            return False
    if stare_curenta not in graf:
        return False
    for muchie in graf[stare_curenta]:
        if muchie.value == secventa[pos_secventa]:
            result = parcurgere_accepta(graf, muchie.destination, secventa, pos_secventa + 1, stari_finale)
            if result:
                return True
    return False


class Muchie:
    def __init__(self, destination, value):
        self.destination = destination
        self.value = value

    def __str__(self):
        print("{} {}".format(self.destination, self.value))


class AFD:
    def __init__(self):
        self.__graf = {}

    def reInit(self, muchii, stari_initiale, stari_finale):
        self.__graf = self.__create_graf(muchii)
        self.__stari_initiale = stari_initiale
        self.__stari_finale = stari_finale
        self.__multimea_starilor = self.__createMultime(muchii)

    @staticmethod
    def __create_graf(muchii):
        graf = {}
        for muchie in muchii:
            key = muchie[0]
            if key not in graf:
                graf[key] = []
            graf[key].append(Muchie(muchie[1], muchie[2]))
        return graf

    def get_multimea_starilor(self):
        return self.__multimea_starilor

    def get_alfabet(self):
        alfabet = []
        for el in self.__graf.keys():
            for muchie in self.__graf[el]:
                if muchie.value not in alfabet:
                    alfabet.append(muchie.value)
        return alfabet

    def get_tranzitii(self):
        tranzitii = []
        for el in self.__graf.keys():
            for tranzitie in self.__graf[el]:
                tranzitii.append([el, tranzitie.destination, tranzitie.value])
        return tranzitii

    def get_stari_finale(self):
        return self.__stari_finale

    @staticmethod
    def __createMultime(muchii):
        multime = []
        for muchie in muchii:
            if muchie[0] not in multime:
                multime.append(muchie[0])
            if muchie[1] not in multime:
                multime.append(muchie[1])
        return multime

    def accepta(self, secventa):

        for stare in self.__stari_initiale:
            stare_curenta = stare
            value = parcurgere_accepta(self.__graf, stare_curenta, secventa, 0, self.__stari_finale)
            if value:
                return True
        return False

    def prefix_maxim(self, secventa):
        for stare in self.__stari_initiale:
            stare_curenta = stare
            index = parcurgere(self.__graf, stare_curenta, secventa, 0)
            print(index)
            return secventa[:index]
