---
name: polish-linguist
description: Polish language expert for flashcard creation, validation, and dataset auditing. Includes orthography rules (ó/u, rz/ż, ch/h), punctuation, capitalization, "nie" spelling, and online dictionary lookup via sjp.pwn.pl.
license: MIT
compatibility: opencode
metadata:
  language: polish
  domain: linguistics
---

# Polish Linguist — Mistrz Polszczyzny 2026

Unified skill for working on the Mistrz Polszczyzny flashcard application. Covers project architecture, code conventions, Polish language rules, online dictionary tools, and card validation procedures.

---

## 1. Project at a Glance

| Aspect         | Detail                                                        |
|----------------|---------------------------------------------------------------|
| **Type**       | Static web app (HTML/CSS/JS) — no frameworks, no bundlers     |
| **Purpose**    | Flashcard tool for learning Polish orthography & punctuation   |
| **Dataset**    | 400 cards across 10 categories                                 |
| **Persistence**| `localStorage` keys: `mistrz_errors`, `mistrz_state`          |
| **Language**   | Communicate with users in Polish; code comments in English OK  |

### Key Files

| File                    | Role                                          | Editable? |
|-------------------------|-----------------------------------------------|-----------|
| `index.html`            | App entry point                               | Yes       |
| `style.css`             | Styles, dark mode, responsiveness             | Yes       |
| `script.js`             | App logic, state, LocalStorage                | Yes       |
| `data.js`               | Flashcard database (400 cards)                | Yes       |
| `generate_full_data.py` | Legacy build script (not used in current workflow) | Yes  |

---

## 2. Build & Run

```bash
# Serve locally
python3 -m http.server 8000
```

**Data editing workflow:**
1. Edit `data.js` directly — it contains all 400 cards
2. Run validation checks (see section 13) after any edit
3. Verify the file loads correctly: `node -e "console.log(require('./data.js').length)"`

---

## 3. Code Style

### JavaScript (`script.js`)
- Vanilla ES6+, 4-space indent, always use semicolons
- `const` by default, `let` for mutable state, never `var`
- `camelCase` naming; DOM access via `const $ = (sel) => document.getElementById(sel);`
- State in globals (`currentIndex`, `errorIds`, `currentDeck`); call `saveState()`/`saveErrors()` after mutations
- `try...catch` around `localStorage` and JSON operations

### CSS (`style.css`)
- Plain CSS with Custom Properties in `:root` (`--bg`, `--surface`, `--accent`, `--text`)
- Flexbox layout, mobile-first, `.app` max-width 440px
- `rem` for font sizes, `px` for borders/radius, 4-space indent

### HTML (`index.html`)
- Semantic HTML5, 4-space indent, double-quoted attributes
- Buttons must have readable text or `aria-label`

### Python (`generate_full_data.py`)
- PEP 8, 4-space indent, `encoding='utf-8'` on all file ops, f-strings

---

## 4. Flashcard Data Format

Each card is a JavaScript object:

```javascript
{ id: 123, category: "Ortografia ó/u", front: "St___ł", back: "Stół", rule: "Ó→O (stół→stołu)." }
```

| Field      | Requirements                                                                    |
|------------|---------------------------------------------------------------------------------|
| `id`       | Unique integer across the entire dataset                                        |
| `category` | Must be one of the 10 allowed categories (see below)                            |
| `front`    | Question — word with `___` (always 3 underscores) or choice format              |
| `back`     | Correct answer — full word or expression                                        |
| `rule`     | Short Polish justification, ends with `.`, no trailing commas before period      |

### `front` Conventions by Category

| Category type          | Convention                                                     |
|------------------------|----------------------------------------------------------------|
| Ortografia (ó/u, rz/ż, ch/h) | `___` replaces the tested letter/digraph                 |
| Pisownia "nie"         | "Nie X czy NieX" or "(Nie)X"                                   |
| Interpunkcja           | "Zdanie: ... ___ ..." — student decides on comma               |
| Rozprawka/Opowiadanie  | Full expression, optionally `[?]` for punctuation              |
| Wielka/mała litera     | `___` replaces the first letter of the word                    |

### Forbidden Anti-Patterns in `front`

- `front` must NOT reveal the answer (e.g. `Pe___ch` shows "ch" — use `Pe___`)
- `front` must NOT reveal the digraph (e.g. `Sztukmi___trz` shows "trz" — use `Sztukmi___`)
- No parenthetical hints like "(akwen)" unless absolutely necessary for homonym disambiguation

---

## 5. Allowed Categories

| Category               | Tests                                              |
|------------------------|----------------------------------------------------|
| `Interpunkcja`         | Commas before conjunctions, compound sentences      |
| `Ortografia ó/u`       | Spelling ó vs u                                    |
| `Ortografia rz/ż`      | Spelling rz vs ż                                   |
| `Ortografia ch/h`      | Spelling ch vs h                                   |
| `Pisownia 'nie'`       | Joint vs separate spelling of "nie"                |
| `Rozprawka`            | Phrases and punctuation in argumentative writing    |
| `Opowiadanie`          | Narrative expressions and their punctuation         |
| `Wielka litera`        | Proper nouns requiring capital letters              |
| `Mała litera`          | Words written lowercase (adjectives, months)        |
| `Poprawność językowa`  | Most common errors and correct forms                |

---

## 6. Polish Language Rules — Orthography

### 6.1 Ó vs U

**Write Ó when:**
- Alternates with **o**, **e**, or **a** (stół→stołu, mówić→mowa, wrócić→wracać)
- In the ending **-ów** (domów, kotów)
- Exceptions at word start: **ósmy**, **ówczesny**

**Write U when:**
- At word start (ustawa, uczeń, uwaga)
- In endings **-utki**, **-uś**, **-uśki** (malutki, maluśki)
- No alternation to another vowel (but, klucz, kura, mur)
- Exceptions: skuwka, zasuwka, wsuwka — U despite phonetic ending

**Critical:** Only create ó/u cards for words where students genuinely confuse the two. `Dom` (nobody writes "dóm") or `Pora` (nobody writes "póra") are invalid.

### 6.2 RZ vs Ż

**Write RZ when:**
- Alternates with **r** (rzeka→rzeczny, morze→morski, burza→burzyć)
- After consonants: **b, p, d, t, g, k, ch, j, w** (brzoza, przygoda, drzewo, trzeba, krzak)
- In endings: **-arz**, **-erz**, **-mierz**, **-mistrz** (malarz, kołnierz, sztukmistrz)

**Write Ż when:**
- Alternates with **g, z, s, dz, h, ź** (droga→dróżka, wskazać→wskażę, druh→drużyna)
- In foreign words (żyrafa, inżynier)
- After **l, ł, n** (lżej, małżonka, rewanż)
- In endings **-aż**, **-eż/-ież** (garaż, młodzież)

**Critical:** rz/ż cards must test rz or ż specifically — not sz, ł, ź, or other digraphs.

### 6.3 CH vs H

**Write CH when:**
- Alternates with **sz** (mucha→muszka, suchy→susza, cicho→cisza)
- After **s** (schować, scharakteryzować, wyschnąć)
- At word end (dach, puch, mech, strach, brzuch, śmiech)
- Traditional spelling (chleb, chłopiec, chmura, chwila, chcieć)

**Write H when:**
- Alternates with **ż** (druhna→drużyna)
- After **z** (zharmonizować, zhańbić)
- In foreign words (historia, hotel, humor, hałas, herbata, hipoteza, horyzont)
- Exception: **druh** — H at word end

---

## 7. Polish Language Rules — Punctuation

### Comma required before:
że, żeby, czy (repeated), co, który, ponieważ, kiedy, jak, jaki, jednak, gdy, gdzie, bo, by, aby, ale, więc, zatem, toteż, dlatego, lecz, czyli, natomiast, zaś

### No comma before:
i, oraz, albo, lub, ani, czy (single use), zarazem, także, bądź

### Comma-shifting rule:
In compounds **mimo że, szczególnie gdy, jako że, podczas gdy, tym bardziej że** — place comma BEFORE the entire phrase, not before the conjunction alone.

### Adverbial participle:
Always separated by comma: "Idąc do szkoły**,** kupił gazetę."

---

## 8. Polish Language Rules — Spelling of "nie"

| Part of speech                             | Spelling   | Example                        |
|--------------------------------------------|-----------|--------------------------------|
| Verb                                       | SEPARATE  | nie wiem, nie mogę, nie lubię  |
| Noun                                       | JOINT     | nieład, niepokój, nienawiść    |
| Adjective (positive degree)                | JOINT     | nieładny, niemiły, niezwykły   |
| Adjective (comparative/superlative)        | SEPARATE  | nie lepszy, nie najlepszy      |
| Adjectival adverb (positive)               | JOINT     | niechętnie                     |
| Non-adjectival adverb                      | SEPARATE  | nie bardzo, nie dziś           |
| Adjectival participle                      | JOINT     | niepalący                      |
| Adverbial participle                       | SEPARATE  | nie czekając                    |
| Numeral                                    | SEPARATE  | nie trzy (exception: niejeden) |
| Pronoun                                    | SEPARATE  | nie ja, nie ten                |

**Exceptions — verbs written jointly:** niepokoić, nienawidzić, niedomagać

---

## 9. Polish Language Rules — Capitalization

**Capital letter:** names, surnames, nicknames, countries, cities, rivers, mountains, seas, continents, planets, holidays, institutions, offices, streets, inhabitants of countries/regions (Polak, Pomorzanin), possessive adjectives from names (Sienkiewiczowski).

**Lowercase:** adjectives from geographic names (polski, warszawski), months and days of week, city inhabitants (warszawiak, krakowianin), historical epoch names (średniowiecze).

---

## 10. Common Language Errors

| Error                  | Correct form            | Why                           |
|------------------------|-------------------------|-------------------------------|
| wziąść / wziołem       | wziąć / wziąłem         | Correct root inflection        |
| w dniu dzisiejszym     | dzisiaj                 | Pleonasm / officialese         |
| przekonywujący         | przekonujący            | Hybrid word formation          |
| okres czasu            | okres / czas            | Pleonasm                       |
| odnośnie tego          | odnośnie do tego        | Requires preposition "do"      |
| tą książkę             | tę książkę              | Correct accusative             |
| chcieli by             | chcieliby              | "-by" joined with verb         |

---

## 11. Online Reference Tools

Use these online dictionaries and resources to verify spelling, inflection, and rules when creating or auditing flashcards. Agents with web access should fetch these URLs directly to confirm correctness.

### Primary: Slownik Jezyka Polskiego PWN (sjp.pwn.pl)

The authoritative source for Polish language. Updated with the 2026 orthography reform.

| Resource                        | URL pattern                                      | Use for                                     |
|---------------------------------|--------------------------------------------------|---------------------------------------------|
| **Orthographic dictionary**     | `https://sjp.pwn.pl/so/{word}`                   | Spelling, inflection forms, hyphenation      |
| **General dictionary (definitions)** | `https://sjp.pwn.pl/slowniki/{word}`        | Definitions, checking if a word exists       |
| **Spelling & punctuation rules**| `https://sjp.pwn.pl/zasady`                      | Official orthography and punctuation rules   |
| **Language advisory (Poradnia)**| `https://sjp.pwn.pl/poradnia`                    | Expert answers on tricky language questions   |
| **Confusing words (Slowa mylone)** | `https://sjp.pwn.pl/ciekawostki/Slowa-mylone;204475.html` | Commonly confused word pairs    |
| **Spelling traps (Pulapki ortografii)** | `https://sjp.pwn.pl/ciekawostki/Pulapki-ortografii;204474.html` | Known spelling pitfalls |
| **Doroszewski dictionary**      | `https://sjp.pwn.pl/doroszewski/{word}`          | Historical definitions, etymology            |

**Example — verify "stol" spelling:**
```
Fetch: https://sjp.pwn.pl/so/stół
→ Returns inflection: stół, stołu, stole; stołów
→ Confirms ó with alternation rule [5] 2.1
```

### Secondary: SJP.pl (Community dictionary)

| Resource                        | URL pattern                                      | Use for                                     |
|---------------------------------|--------------------------------------------------|---------------------------------------------|
| **Word lookup**                 | `https://sjp.pl/{word}`                          | Quick existence check, Scrabble validity     |

Open-source community dictionary. Useful for quick checks but not as authoritative as PWN. Good for verifying whether a word form exists in common usage.

### Supplementary: SGJP (Grammatical Dictionary of Polish)

| Resource                        | URL pattern                                      | Use for                                     |
|---------------------------------|--------------------------------------------------|---------------------------------------------|
| **Inflection lookup**           | `https://sgjp.pl/leksemy/`                       | Full inflection tables, grammatical forms    |

Academic grammatical dictionary (Saloni, Wolinski et al., 4th edition). Provides complete inflection paradigms for every word — useful when you need to verify all declined/conjugated forms (e.g., confirming that "stol" → "stolu" is a valid alternation).

### How to Use in Validation

When validating a flashcard (section 12), use these tools at the following steps:

1. **Step 1 (`back` correctness)** — Fetch `https://sjp.pwn.pl/slowniki/{word}` to confirm the word exists
2. **Step 3 (rule correctness)** — Fetch `https://sjp.pwn.pl/so/{word}` to verify the phonetic alternation cited in `rule`
3. **Step 3 (realistic error)** — Check `https://sjp.pwn.pl/ciekawostki/Pulapki-ortografii;204474.html` to see if the word is a known spelling pitfall
4. **Disputed cases** — Search `https://sjp.pwn.pl/poradnia` for expert rulings on ambiguous forms

---

## 12. Card Validation Checklist

Run these checks when creating or reviewing any flashcard:

1. **`back` correctness** — Is it a real Polish word? Fetch `https://sjp.pwn.pl/slowniki/{word}` to confirm.
2. **Category match** — Does the card test exactly the letter pair its category declares? (ó/u tests only ó vs u; rz/ż tests only rz vs ż; ch/h tests only ch vs h)
3. **`front` quality** — Does `___` hide the right letter/digraph? No answer leaks? No parenthetical hints? Would a student realistically make this mistake?
4. **`rule` correctness** — Factually correct? Written in Polish? Ends with `.`? No trailing comma before period? Fetch `https://sjp.pwn.pl/so/{word}` to verify phonetic alternation.
5. **No duplicates** — `front` unique across dataset? No other card with same `back`?
6. **`front` ↔ `back` consistency** — Inserting the correct letter into `___` produces the `back` word? Lengths match?

---

## 13. Procedures

### Adding a New Card

1. Choose a word where students **realistically make errors**
2. Verify spelling via `https://sjp.pwn.pl/so/{word}` — confirm the word exists and check inflection
3. Establish the rule — provide phonetic alternation or principle
4. Format `front` per conventions (always `___`, three underscores)
5. Assign the next available `id`
6. Run the validation checklist (section 12)
7. Add to `data.js` directly
8. Verify with `node -e "console.log(require('./data.js').length)"`

### Dataset Audit

```bash
# 1. Check for duplicate fronts
python3 -c '
import re
with open("data.js") as f:
    content = f.read()
cards = re.findall(r"id: (\d+).*?front: \"([^\"]+)\".*?back: \"([^\"]+)\"", content)
fronts = {}
for id_, front, back in cards:
    if front in fronts:
        fronts[front].append((id_, back))
    else:
        fronts[front] = [(id_, back)]
for front, entries in fronts.items():
    if len(entries) > 1:
        print(f"DUPLIKAT: \"{front}\" → {entries}")
if not any(len(v) > 1 for v in fronts.values()):
    print("Brak duplikatów.")
print(f"Łącznie fiszek: {len(cards)}")
'

# 2. Check for trailing commas in rules
python3 -c '
import re
with open("data.js") as f:
    content = f.read()
cards = re.findall(r"id: (\d+).*?rule: \"([^\"]+)\"", content)
for id_, rule in cards:
    if rule.endswith(",.") or rule.endswith(","):
        print(f"id {id_}: trailing przecinek w regule: \"{rule}\"")
'

# 3. Check if front leaks the answer (heuristic)
python3 -c '
import re
with open("data.js") as f:
    content = f.read()
cards = re.findall(r"id: (\d+).*?category: \"([^\"]+)\".*?front: \"([^\"]+)\".*?back: \"([^\"]+)\"", content)
for id_, cat, front, back in cards:
    if "rz/ż" in cat:
        clean = front.replace("___", "")
        if "rz" in clean.lower() or "ż" in clean.lower():
            print(f"id {id_}: front odsłania rz/ż: \"{front}\" → \"{back}\"")
    if "ch/h" in cat:
        clean = front.replace("___", "")
        if "ch" in clean.lower() and "ch" in back.lower():
            print(f"id {id_}: front odsłania ch: \"{front}\" → \"{back}\"")
'
```

---

## 14. Testing Checklist

- Card flipping works correctly
- "Umiem" vs "Powtórzę" logic functions properly
- "Do powtórki" mode filters cards correctly
- Page reload preserves progress via `localStorage`
- "Resetuj postępy" button clears all saved state
- Mobile layout renders correctly (test at 440px width)
- Dark mode colors have sufficient contrast
