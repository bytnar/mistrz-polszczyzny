# Mistrz Polszczyzny 2026

## Opis aplikacji

**Mistrz Polszczyzny 2026** to aplikacja webowa typu flashcard do nauki poprawnej polskiej ortografii i interpunkcji, zaprojektowana specjalnie dla uczniów przygotowujących się do pisania wypracowań (opowiadań i rozprawek).

## Główne funkcje

### 📚 300 unikalnych fiszek
Aplikacja zawiera **300 starannie dobranych przykładów** podzielonych na kategorie:
- **Interpunkcja** (60 fiszek) - zasady stawiania przecinków przed spójnikami (że, ponieważ, mimo że, chyba że)
- **Ortografia ó/u** (60 fiszek) - wymiana ó↔o, rozróżnianie ó/u
- **Ortografia rz/ż** (60 fiszek) - wymiana rz↔r, ż↔g, pisownia po spółgłoskach
- **Ortografia ch/h** (40 fiszek) - wymiana ch↔sz, wyrazy obce z h
- **Pisownia 'nie'** (40 fiszek) - łączna i rozdzielna pisownia z różnymi częściami mowy
- **Rozprawka** (20 fiszek) - zwroty typowe dla tekstów argumentacyjnych
- **Opowiadanie** (10 fiszek) - wyrażenia narracyjne
- **Wielka litera** (10 fiszek) - nazwy własne, geograficzne

### 🎯 System nauki
- **Flip card** - kliknij fiszkę, aby zobaczyć odpowiedź i zasadę
- **Tracking błędów** - oznacz trudne fiszki przyciskiem "Powtórzę"
- **Tryb powtórek** - ćwicz tylko zaznaczone fiszki
- **LocalStorage** - postępy zapisywane lokalnie w przeglądarce
- **Progress bar** - wizualizacja postępów (np. "5 / 300")

### 📱 Design
- **Mobile-first** - zoptymalizowana pod iPhone
- **Dark mode** - nowoczesny ciemny motyw
- **Minimalistyczny UI** - czytelny interfejs bez rozpraszaczy
- **Safe area support** - kompatybilność z notch i home indicator

## Technologie

- **HTML5** - struktura
- **Vanilla CSS** - stylowanie (bez frameworków)
- **Vanilla JavaScript** - logika aplikacji
- **LocalStorage API** - persystencja danych

## Pliki projektu

```
mistrz-polszczyzny/
├── index.html      # Struktura aplikacji
├── style.css       # Stylowanie (dark mode, mobile-first)
├── script.js       # Logika (state management, LocalStorage)
├── data.js         # 300 fiszek z przykładami
├── jpd.md          # Dokumentacja produktu
└── AGENTS.md       # Ten plik
```

## Jak używać

1. Otwórz `index.html` w przeglądarce
2. Kliknij fiszkę, aby zobaczyć odpowiedź
3. Wybierz "Umiem" (następna karta) lub "Powtórzę" (zaznacz do powtórki)
4. Przełącz na tryb "Do powtórki", aby ćwiczyć tylko trudne fiszki
5. Użyj "Resetuj postępy", aby wyczyścić zaznaczenia

## Status projektu

✅ **Gotowe do użycia**
- 300 unikalnych fiszek (zweryfikowane - brak duplikatów)
- Pełna funkcjonalność (tracking, review mode, reset)
- Responsywny design (mobile + desktop)
- Testy przeglądarki zakończone sukcesem

## Autor

Projekt stworzony z pomocą **Antigravity AI** (Google Deepmind).

## Kompendium Poprawności Językowej

Poniżej znajduje się skrót najważniejszych zasad językowych, które warto znać przygotowując się do matury i egzaminów.

### 1. Interpunkcja: Przecinek jako Narzędzie Precyzji

*   **W zdaniach złożonych:** Należy oddzielać zdania składowe (zasada: każda czynność/czasownik wymaga oddzielenia).
*   **Przed spójnikami:** Przecinek stawiamy przed: że, żeby, czy, co, który, ponieważ, kiedy, jak, jednak, gdy, gdzie, bo, by, aby, ale, więc, zatem, toteż, dlatego, lecz, czyli, natomiast, zaś.
*   **Imiesłowy:** Zawsze oddzielamy czasownik od imiesłowu przysłówkowego (-ąc, -wszy).

**Kiedy nie stawiamy przecinka?** Przed spójnikami współrzędnymi: i, oraz, albo, lub, ani, czy, zarazem, także, bądź.

### 2. Ortografia w Pigułce

**Rz vs Ż**
*   **Rz:** Piszemy, gdy wymienia się na r (tworzyć – twórca) oraz po spółgłoskach (np. drzewo, krzak).
*   **Ż:** Piszemy w cząstkach ża-, żo-, żu-, ży- oraz gdy wymienia się na: g, z, s, dz, h, ź (dróżka – droga).

**Ch vs H**
*   **Ch:** Piszemy, gdy wymienia się na sz (cicho – cisza), po spółgłosce s (scharakteryzować) oraz na końcu wyrazu.
*   **H:** Piszemy, gdy wymienia się na ż (druhna – drużyna).

**Ó vs U**
*   **Ó:** Piszemy, gdy wymienia się na o, e, a oraz w końcówkach -ów.
*   **U:** Piszemy na początku wyrazu (ustawa) oraz w zakończeniach -utki, -uś.

### 3. Poprawność Językowa - Najczęstsze błędy

| Błąd | Poprawna forma | Dlaczego? |
| :--- | :--- | :--- |
| w dniu dzisiejszym | dzisiaj | Unikanie urzędowego żargonu. |
| wziąść | wziąć | Poprawna fleksja. |
| przekonywujący | przekonujący | Eliminacja hybrydy. |
| okres czasu | okres / czas | Pleonazm ("masło maślane"). |
| odnośnie tego | odnośnie do tego | Wymagany przyimek "do". |
| bynajmniej (= przynajmniej) | bynajmniej (= wcale) | Bynajmniej to partykuła przecząca! |

### 4. Wielka i Mała Litera

*   **Wielka:** Imiona, nazwiska, nazwy państw, miast, rzek, planet, świąt, instytucji.
*   **Mała:** Przymiotniki od nazw geograficznych (polski, warszawski), nazwy miesięcy, dni tygodnia, mieszkańców miast (warszawiak).
