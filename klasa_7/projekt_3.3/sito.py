""" Sito Eratostenesa
    Znajdywanie liczb pierwszych w zbiorze metodą sita Eratostenesa.
    Zadanie 3.3 z informatyki klasy 7 szkoły podstawowej. Wydanie II zmienione z roku 2020.
    Podręcznik autorstwa
      - Wanda Jochemczyk
      - Iwona Krajewska-Kranas,
      - Witold Kranas
      - Mirosław Wyczółkowski
"""

def usun_wielokrotnosci(co):
  """ Usuwa wielokrotności zaczynając od indeksu równego 'co' """
  print(f"analizuję {co}")
  # w pythonie listy są indeksowane od zera
  index = co -1
  # pętla for zawsze startuje od zera, dlatego należy użyć while
  while index < len(liczby):
    print(f" sprawdzam index: {index} (liczba {liczby[index]})")
    if not (liczby[index] == 0):
      if (liczby[index] % co == 0):
        print(f" jest wielokrotność!")
        if not (liczby[index] == co):
          print(f" skreślam: {liczby[index]}")
          # w oryginalnym zadaniu w Scratchu używało się 'x', ale w Pythonie oznaczałoby to konieczność konwersji typu
          liczby[index] = 0
        else:
          print(f" to ta sama liczba więc omijam")
    else:
      print(f" skreślone")
    index += 1
    print(f" Lista: {liczby}\n")

def znajdz_wyniki():
  for l in liczby:
    if not (l == 0):
      wyniki.append(l)

def drukuj_wyniki():
  print(f"Znaleziono {len(wyniki)} liczb pierwszych. Oto one:")
  for w in wyniki:
    print(w)

if __name__ == "__main__":
  liczby = []
  wyniki = []

  zakres = int(input("Podaj ile elementów chcesz sprawdzić: "))
  # range działa bez ostatniego elementu
  for liczba in range(1, zakres+1):
    liczby.append(liczba)

  print(f"Początkowa lista:")
  print(f"{liczby}")

  # skreślamy pierwszy element listy i bierzemy drugi
  liczby[0] = 0
  dzielnik = liczby[1]
  # aby nie wyjśc poza zakres listy
  while (dzielnik*dzielnik) < len(liczby):
    if not (liczby[dzielnik -1] == 0):
      usun_wielokrotnosci(dzielnik)
    dzielnik += 1
  znajdz_wyniki()
  drukuj_wyniki()

# the end