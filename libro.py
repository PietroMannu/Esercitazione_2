class Libro:
    def __init__(self, titolo: str, autore: str, anno: int, editore: str, pagine: int):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def readingTime(self) -> float:
        # Consideriamo una media di 2 minuti per pagina (risultato in minuti)
        return self.pagine * 2

    def __str__(self):
        return f"'{self.titolo}' - {self.autore} ({self.anno}, {self.editore}) - {self.pagine} pag."