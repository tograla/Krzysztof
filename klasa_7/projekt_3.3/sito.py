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
  # w pythonie listy są indeksowane od zera
  index = co -1
  skreslenia = 0
  # pętla for zawsze startuje od zera, dlatego należy użyć while
  while index < len(liczby):
    print(f"sprawdzam index: {index} (liczba {liczby[index]})")
    if not (liczby[index] == 0):
      if (liczby[index] % co == 0):
        print(f" jest wielokrotność!")
        if not (liczby[index] == co):
          print(f" skreślam: {liczby[index]}")
          # w oryginalnym zadaniu w Scratchu używało się 'x', ale w Pythonie oznaczałoby to konieczność konwersji typu
          liczby[index] = 0
          skreslenia += 1
        else:
          print(f" to ta sama liczba więc omijam")
      else:
        print(f" to nie wielokrotność")
    else:
      print(f" już skreślone, omijam")
    index += 1
  return skreslenia

def znajdz_wyniki():
  """ Wybieramy nieskreślone elementy z listy liczby """
  for l in liczby:
    if not (l == 0):
      wyniki.append(l)

def drukuj_wyniki():
  """ Drukujemy w wierszach po 10 elementów """
  print(f"Znaleziono {len(wyniki)} liczb pierwszych. Oto one:")
  for i,v in enumerate(wyniki):
    print(f"{v:4}, ", end='')
    if ((i+1)%10 == 0):
      print("")

def ustaw_zakres():
  """ Pobiera zakres do przesiewania """
  while True:
    zakres = int(input("Podaj ile elementów chcesz sprawdzić: "))
    if int(zakres) > 0: break
  # range działa bez ostatniego elementu
  for liczba in range(1, zakres+1):
    liczby.append(liczba)
  print(f"Początkowa lista:")
  print(f"{liczby}")

if __name__ == "__main__":
  liczby = []
  wyniki = []
  ustaw_zakres()
  # skreślamy pierwszy element listy i bierzemy drugi
  liczby[0] = 0
  dzielnik = liczby[1]
  # aby nie wyjśc poza zakres listy
  while (dzielnik*dzielnik) < len(liczby):
    print(f"DZIELNIK: {dzielnik}")
    if not (liczby[dzielnik-1] == 0):
      skreslenia = usun_wielokrotnosci(dzielnik)
    else:
      print(f" Ta liczba jest wielokrotnością wcześniejszej, zatem została już wykreślona.")
    print(f" Razem skreśleń: {skreslenia}.\n Lista po wykreśleniu liczby {dzielnik}: {liczby}\n")
    skreslenia = 0
    dzielnik += 1
  znajdz_wyniki()
  drukuj_wyniki()

# the end