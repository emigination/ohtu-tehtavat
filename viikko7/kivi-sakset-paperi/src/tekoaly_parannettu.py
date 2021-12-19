from collections import deque

class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = deque()
        self._muistin_koko = muistin_koko

    def aseta_siirto(self, siirto):
        if len(self._muisti) == self._muistin_koko:
            self._muisti.popleft()
        self._muisti.append(siirto)

    def anna_siirto(self):
        if len(self._muisti) <= 1:
            return "k"

        viimeisin_siirto = self._muisti[len(self._muisti)-1]

        seuraavat = {'k': 0, 's': 0, 'p': 0}

        for i in range(len(self._muisti)-1):
            if self._muisti[i] == viimeisin_siirto:
                seuraavat[self._muisti[i + 1]]+=1

        eniten = max(seuraavat, key=seuraavat.get)
        if eniten == 'k':
            return 'p'
        if eniten == 'p':
            return 's'
        return 'k'
