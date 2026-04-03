#PARTE 1
print("------Stampa di variabili di esempio:------")
titlo = "Il signiore degli anelli"
n_copie = 10
prezzo = 10.99
stato = 1

print(f"Titolo: {titlo}")
print(f"Numero di copie: {n_copie}")
print(f"Prezzo: {prezzo}")
print(f"Stato: {"Disponibile" if stato == 1 else "Non disponibile"}")

print("\n")

#PARTE 2
titoli_libri = ["Il signiore degli anelli", "La notte dei tempi", "La città perduta", "La macchina del tempo", "Il potere della mente"]
n_copie_libri = {"Il signiore degli anelli": 10, "La notte dei tempi": 5, "La città perduta": 3, "La macchina del tempo": 2, "Il potere della mente": 1}
utenti_registrati = {"Mario", "Luigi", "Giovanni", "Francesco", "Marco", "Diego"}

#PARTE 3
class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}"


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"Scheda utente: [Nome: {self.nome}, Età: {self.eta}, ID utente: {self.id_utente}]"


class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        return f"Dettagli prestito: [Utente: {self.utente.nome}, Libro: {self.libro.titolo}, Giorni: {self.giorni}]"

class NessunaCopiaDisponibileError(Exception):
    def __init__(self, titolo_libro):
        super().__init__(f"Nessuna copia disponibile per il libro: {titolo_libro}")
        self.titolo_libro = titolo_libro


def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili <= 0:
        raise NessunaCopiaDisponibileError(libro.titolo)

    libro.copie_disponibili -= 1
    return Prestito(utente, libro, giorni)



libro1 = Libro("Il signiore degli anelli", "J.R.R. Tolkien", 1954, 10)
libro2 = Libro("La notte dei tempi", "René Barjavel", 1968, 5)
libro3 = Libro("La macchina del tempo", "H.G. Wells", 1895, 2)

libri = [libro1, libro2, libro3]

print("------Libri:------")
for libro in libri:
    print(libro.info())

utente1 = Utente("Mario", 30, 1)
utente2 = Utente("Giovanni", 25, 2)
utente3 = Utente("Francesco", 40, 3)

utenti = [utente1, utente2, utente3]

print("\n")
print("------Utenti:------")
for utente in utenti:
    print(utente.scheda())

prestiti = []
try:
    prestito1 = presta_libro(utente1, libro1, 10)
    prestiti.append(prestito1)
except NessunaCopiaDisponibileError as e:
    print(e)

try:
    prestito2 = presta_libro(utente2, libro2, 10)
    prestiti.append(prestito2)
except NessunaCopiaDisponibileError as e:
    print(e)
    
try:
    prestito3 = presta_libro(utente3, libro3, 10)
    prestiti.append(prestito3)
except NessunaCopiaDisponibileError as e:
    print(e)

print("\n")
print("------Dettaglo prestiti:------")
for prestito in prestiti:
    print(prestito.dettagli())

print("\n")
print("------Dettaglo libri:------")
for libro in libri:
    print(libro.info())

