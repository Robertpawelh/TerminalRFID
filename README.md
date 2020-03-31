# TerminalRFID

## Uruchomienie projektu
Pobieramy projekt i uruchamiamy plik main.py

## Elementy składowe
```data/``` - folder zawierający pliki ```.json``` przechowujące dane
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
