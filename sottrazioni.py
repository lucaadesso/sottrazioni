import random

def genera_sottrazione():
  """Genera una sottrazione a 4 cifre."""
  numero1 = random.randint(1000, 9999)
  numero2 = random.randint(1000, numero1 - 1)
  return numero1, numero2

def stampa_sottrazione(numero1, numero2, file=None):
  """Stampa una sottrazione a 4 cifre con un formato specifico."""
  if numero1 is not None:
    print(f"{numero1:4d}\t-\t", file=file, end="")
  else:
    print(f"{numero2:4d}\t\t", file=file, end="")

def main():
  """Genera e stampa 5 sottrazioni a 4 cifre in un file."""
  numeri1 = []
  numeri2 = []
  with open("sottrazioni.txt", "a") as file:  # Apri il file in scrittura
    file.write("\n")  # Aggiungi una linea vuota
    for _ in range(5):
      numero1, numero2 = genera_sottrazione()
      numeri1.append(numero1)
      numeri2.append(numero2)
      stampa_sottrazione(numero1, None, file)  # Stampa in file
    file.write("\n")  # Aggiungi una linea vuota

    for numero2 in numeri2:
      stampa_sottrazione(None, numero2, file)  # Stampa in file
    file.write("\n")  # Aggiungi una linea vuota

    file.write("\t\t".join(["-------" for _ in range(5)]))  # Linea di trattini
    file.write("\n")  # Aggiungi una linea vuota
    file.write("\n")  # Aggiungi una linea vuota
    file.write("\t\t".join(["'=====" for _ in range(5)]))  # Linea di uguali
    file.write("\n")  # Aggiungi una linea vuota

if __name__ == "__main__":
  main()