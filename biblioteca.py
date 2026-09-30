from libro import Libro

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.libri = []

    def inserisci_libro(self, libro: Libro):
        self.libri.append(libro)

    def cerca_per_titolo(self, titolo: str):
        return [l for l in self.libri if titolo.lower() in l.titolo.lower()]

    def conteggio() -> int:
        return len(self.libri)