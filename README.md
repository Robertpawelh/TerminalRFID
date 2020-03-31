# TerminalRFID

## Uruchomienie projektu
* Pobieramy program 
* Uruchamiamy plik ```main.py```, wpisując w konsoli ```python main.py```, będąc w katalogu TerminalRFID

## Elementy składowe
```data/``` - folder zawierający pliki ```.json``` przechowujące dane

```screens/``` - zrzuty ekranu przedstawiające przykładowe działanie aplikacji

Dane są przechowywane w formie słownika, którego kluczami są indywidualne identyfikatory, natomiast wartościami dane o danym elemencie

Przykładowy plik ```data/workers.json```
```
{
  "309682750991167982376509968972305895365": {
    "name": "Adam Nowak",
    "card_id": "[173, 124, 223, 37, 41]"
  },
  "320655828206313813939240752188416561093": {
    "name": "Jan Kowalski",
    "card_id": null
  }
}
```

```data_operations.py``` - plik zawiera funkcje operujące na danych:
* ```read_data``` - parsowanie z JSON
* ```write_data``` - zapisywanie danych do pliku JSON
* ```add_data_to_id``` - dodaje odpowiednie dane do słownika pod określonym ID
* ```remove_data``` - usuwanie danych ze słownika pod określonym ID
* ```add_worker``` - dodawanie nowego pracownika i generowanie mu unikalnego ID
* ```remove_worker``` - usuwanie pracownika o określonym ID
* ```add_card``` - dodawanie karty o określonym ID
* ```remove_card``` - usuwanie karty o określonym ID
* ```add_terminal``` - dodawanie terminalu o określonym ID
* ```remove_terminal``` - usuwanie terminalu o określonym ID
* ```assign_card_id``` - przypisywanie danemu pracownikowi karty
* ```unassign_card_id``` - usuwanie przypisania karty do pracownika
* ```registration``` - zarejestruj odczyt danej karty w danym terminalu
* ```delete_all_data``` - funkcja do resetowania pamięci serwerowej

```logger.py``` - plik zawiera pojedynczą funkcję do wyświetlania wiadomości w konsoli

```main.py``` - plik, który odpowiada za uruchomienie aplikacji

```reports.py``` - plik zawierający funkcje odpowiadające za generowanie raportów

```server_ui.py``` - plik zawierający interfejs użytkownika

## Rejestracja
Rejestracja polega na wyszukaniu pracownika używającego danej karty. Następnie w zależności od tego, czy pracownik ma już wpisaną date przybycia do pracy wpisuje się aktualną datę odpowiednio do tabeli ```begin``` bądź ```end```. Jeśli w bazie brakuje informacji o posiadaczu karty, informacje o odczycie zostają zapisane w tabeli ```UNKNOWN```. 

```
date = str(datetime.now())
```
```
registrations[card_id] = {worker: {'begin': [date], 'begin_t': [terminal_id], 'end': [], 'end_t': []}}
```

## Raporty
Generowanie raportów odbywa się z wykorzystaniem modułu ```csv```.

Po pobraniu identyfikatora pracownika, wyszukiwane są wszystkie karty, z których korzystał dany pracownik.
W raporcie umieszczane są następujące dane:
* identyfikator terminala użytego przy przybyciu pracownika do pracy
* data przybycia pracownika do pracy
* identyfikator terminala użytego przy opuszczeniu miejsca pracy przez pracownika
* data opuszczenia przez pracownika miejsca pracy
* identyfikator użytej karty

```
csv_columns = ["Enter Terminal", "Enter Time", "Exit Terminal", "Exit Time", "Card ID"]
filtered_registrations = dict(filter(lambda x: worker_id in x[1].keys(), registrations.items()))
```

```
writer.writerow([worker_info['begin_t'][i],
                 worker_info['begin'][i],
                 worker_info['end_t'][i],
                 worker_info['end'][i],
                 card_id])
```

## Interfejs użytkownika
UI opiera się głównie na obsłudze wejścia oraz jego błędów. Poprzez wpisywanie cyfr z klawiatury wykonujemy odpowiednie komendy
```
(1). Add terminal
(2). Remove terminal
(3). Assign card to worker
(4). Unassign card from worker
(5). Register
(6). Generate report
(7). Other
(8). Exit
```
Symulacja czytnika kart polega na wyborze numeru karty spośród dostępnych w bazie. Do wyboru są dodatkowo dwie nieistniejące w bazie karty. Następnie wybierany jest terminal i odczyt zostaje zarejestrowany w bazie
