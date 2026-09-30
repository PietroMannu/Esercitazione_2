from libro import Libro
from biblioteca import Biblioteca

def avvia_interfaccia(biblioteca: Biblioteca):
    while True:
        print(f"\n--- INTERFACCIA BIBLIOTECA ({biblioteca.conteggio()} libri in catalogo) ---")
        print("1. Inserisci un nuovo libro")
        print("2. Cerca un libro per titolo")
        print("3. Mostra conteggio totale libri")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            titolo = input("Titolo: ")
            autore = input("Autore: ")
            anno = int(input("Anno di pubblicazione: "))
            editore = input("Editore: ")
            pagine = int(input("Numero pagine: "))

            nuovo_libro = Libro(titolo, autore, anno, editore, pagine)
            biblioteca.inserimento(nuovo_libro)
            print(f"\n[+] Libro inserito! Tempo di lettura stimato: {nuovo_libro.readingTime()} minuti.")

        elif scelta == "2":
            titolo = input("Inserisci il titolo da cercare: ")
            risultati = biblioteca.ricerca(titolo)
            if risultati:
                print("\nLibri trovati:")
                for l in risultati:
                    print(l)
            else:
                print("\nNessun libro trovato con questo titolo.")

        elif scelta == "3":
            print(f"\nLa biblioteca contiene attualmente {biblioteca.conteggio()} libri.")

        elif scelta == "0":
            print("\nUscita dall'interfaccia.")
            break

if __name__ == "__main__":
    mia_biblioteca = Biblioteca("Biblioteca Civica")
    avvia_interfaccia(mia_biblioteca)