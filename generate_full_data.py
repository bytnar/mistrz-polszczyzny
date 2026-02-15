# Read part 1
with open('data_part1.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the closing part
content = content.replace('];', '').replace("if (typeof module !== 'undefined') {\n    module.exports = flashcards;\n}", '')

# Continue from ID 181
additional_cards = []

# === ORTOGRAFIA ch/h (40 cards) ===
chh_data = [
    ("Mu_a", "Mucha", "CH wymienia się na SZ (mucha → muszka)."),
    ("Suc_y", "Suchy", "CH wymienia się na SZ (suchy → susza)."),
    ("Bo_ater", "Bohater", "H w wyrazach obcych."),
    ("_istoria", "Historia", "H w wyrazach obcych."),
    ("Da_", "Dach", "CH na końcu wyrazu."),
    ("Szlo_", "Szloch", "CH na końcu wyrazu."),
    ("Gma_", "Gmach", "CH na końcu wyrazu."),
    ("S_owek", "Schowek", "Po S piszemy CH."),
    ("Z_ardzić", "Zhardzić", "Po Z piszemy H."),
    ("_erbata", "Herbata", "H w wyrazach obcych."),
    ("_umor", "Humor", "H w wyrazach obcych."),
    ("_armonijny", "Harmonijny", "H w wyrazach obcych."),
    ("Sc_ować", "Schować", "Po S piszemy CH."),
    ("Wysc_nąć", "Wyschnąć", "Po S piszemy CH."),
    ("_ałas", "Hałas", "H w wyrazach obcych."),
    ("_ałda", "Hałda", "H w wyrazach obcych."),
    ("_otel", "Hotel", "H w wyrazach obcych."),
    ("_isteria", "Histeria", "H w wyrazach obcych."),
    ("_oryzont", "Horyzont", "H w wyrazach obcych."),
    ("_ipoteza", "Hipoteza", "H w wyrazach obcych."),
    ("C_ory", "Chory", "CH wymienia się na SZ (chory → choroba)."),
    ("C_leb", "Chleb", "CH - tradycyjna pisownia."),
    ("C_łopiec", "Chłopiec", "CH - tradycyjna pisownia."),
    ("C_łodny", "Chłodny", "CH wymienia się na SZ (chłodny → chłód)."),
    ("C_mura", "Chmura", "CH - tradycyjna pisownia."),
    ("C_wila", "Chwila", "CH - tradycyjna pisownia."),
    ("C_wała", "Chwała", "CH - tradycyjna pisownia."),
    ("C_cieć", "Chcieć", "CH - tradycyjna pisownia."),
    ("C_odzić", "Chodzić", "CH - tradycyjna pisownia."),
    ("C_ować", "Chować", "CH - tradycyjna pisownia."),
    ("Uc_o", "Ucho", "CH - tradycyjna pisownia."),
    ("Bruc_", "Brzuch → Bruch", "CH na końcu."),
    ("Smiec_", "Śmiech", "CH na końcu."),
    ("Strec_", "Strach → Strech", "CH na końcu."),
    ("Pac_", "Pach", "CH na końcu."),
    ("Mec_", "Mech", "CH na końcu."),
    ("Tec_", "Tech", "CH na końcu (skrót)."),
    ("_ałaśliwy", "Hałaśliwy", "H w wyrazach obcych."),
    ("_angar", "Hangar", "H w wyrazach obcych."),
    ("_ańba", "Hańba", "H w wyrazach obcych."),
]

for i, (front, back, rule) in enumerate(chh_data, start=181):
    additional_cards.append(f'    {{id: {i}, category: "Ortografia ch/h", front: "{front}", back: "{back}", rule: "{rule}"}},\n')

# === PISOWNIA NIE (40 cards) ===
nie_data = [
    ("__ie wiem", "Nie wiem", "Nie z czasownikami - osobno."),
    ("__ie rozumiem", "Nie rozumiem", "Nie z czasownikami - osobno."),
    ("__ieładny", "Nieładny", "Nie z przymiotnikami (stopień równy) - łącznie."),
    ("__ie lepszy", "Nie lepszy", "Nie z przymiotnikami (stopień wyższy) - osobno."),
    ("__ieład", "Nieład", "Nie z rzeczownikami - łącznie."),
    ("To __ie sztuka.", "To nie sztuka.", "Nie z rzeczownikiem jako orzecznik - osobno."),
    ("__ie mogę", "Nie mogę", "Nie z czasownikami - osobno."),
    ("__ie pamiętam", "Nie pamiętam", "Nie z czasownikami - osobno."),
    ("__iebrzydki", "Niebrzydki", "Nie z przymiotnikami - łącznie."),
    ("__iesłodki", "Niesłodki", "Nie z przymiotnikami - łącznie."),
    ("__ie potrafię", "Nie potrafię", "Nie z czasownikami - osobno."),
    ("__ie umiem", "Nie umiem", "Nie z czasownikami - osobno."),
    ("__iepokój", "Niepokój", "Nie z rzeczownikami - łącznie."),
    ("__ieszczęście", "Nieszczęście", "Nie z rzeczownikami - łącznie."),
    ("__iewiedza", "Niewiedza", "Nie z rzeczownikami - łącznie."),
    ("__ie chcę", "Nie chcę", "Nie z czasownikami - osobno."),
    ("__iemiły", "Niemiły", "Nie z przymiotnikami - łącznie."),
    ("__ie najlepszy", "Nie najlepszy", "Nie z przymiotnikami (stopień najwyższy) - osobno."),
    ("__iedobry", "Niedobry", "Nie z przymiotnikami - łącznie."),
    ("__iezły", "Niezły", "Nie z przymiotnikami - łącznie."),
    ("__ieprawda", "Nieprawda", "Nie z rzeczownikami - łącznie."),
    ("__ienawiść", "Nienawiść", "Nie z rzeczownikami - łącznie."),
    ("__iesprawiedliwość", "Niesprawiedliwość", "Nie z rzeczownikami - łącznie."),
    ("__ie lubię", "Nie lubię", "Nie z czasownikami - osobno."),
    ("__ie mam", "Nie mam", "Nie z czasownikami - osobno."),
    ("__ie jestem", "Nie jestem", "Nie z czasownikami - osobno."),
    ("__ie będę", "Nie będę", "Nie z czasownikami - osobno."),
    ("__ie ma", "Nie ma", "Nie z czasownikami - osobno."),
    ("__ie było", "Nie było", "Nie z czasownikami - osobno."),
    ("__ie można", "Nie można", "Nie z czasownikami - osobno."),
    ("__ie wolno", "Nie wolno", "Nie z czasownikami - osobno."),
    ("__ie trzeba", "Nie trzeba", "Nie z czasownikami - osobno."),
    ("__ie warto", "Nie warto", "Nie z czasownikami - osobno."),
    ("__ie należy", "Nie należy", "Nie z czasownikami - osobno."),
    ("__iekorzystny", "Niekorzystny", "Nie z przymiotnikami - łącznie."),
    ("__iezwykły", "Niezwykły", "Nie z przymiotnikami - łącznie."),
    ("__iezależny", "Niezależny", "Nie z przymiotnikami - łącznie."),
    ("__iebezpieczny", "Niebezpieczny", "Nie z przymiotnikami - łącznie."),
    ("__iezdrowy", "Niezdrowy", "Nie z przymiotnikami - łącznie."),
    ("__iepewny", "Niepewny", "Nie z przymiotnikami - łącznie."),
]

for i, (front, back, rule) in enumerate(nie_data, start=221):
    additional_cards.append(f'    {{id: {i}, category: "Pisownia \'nie\'", front: "{front}", back: "{back}", rule: "{rule}"}},\n')

# === ROZPRAWKA (20 cards) ===
rozpr_data = [
    ("Moim zdan__em", "Moim zdaniem", "Wyrażenie opinii."),
    ("W _ogóle", "W ogóle", "Pisownia rozdzielna."),
    ("Na pe__no", "Na pewno", "Pisownia rozdzielna."),
    ("Konkluduj__c [?]", "Konkludując,", "Imiesłów - przecinek."),
    ("Nale__y podkreślić", "Należy podkreślić", "Czasownik 'należy'."),
    ("Po pierwsze [?]", "Po pierwsze,", "Wyliczenie - przecinek."),
    ("Po drugie [?]", "Po drugie,", "Wyliczenie - przecinek."),
    ("Podsumowuj__c [?]", "Podsumowując,", "Imiesłów - przecinek."),
    ("Z jednej strony [?]", "Z jednej strony,", "Wyrażenie - przecinek."),
    ("Z drugiej strony [?]", "Z drugiej strony,", "Wyrażenie - przecinek."),
    ("Niewątpliwie [?]", "Niewątpliwie,", "Przysłówek - przecinek."),
    ("Bezsprzecznie [?]", "Bezsprzecznie,", "Przysłówek - przecinek."),
    ("Oczywiście [?]", "Oczywiście,", "Przysłówek - przecinek."),
    ("Naturalnie [?]", "Naturalnie,", "Przysłówek - przecinek."),
    ("Zapewne [?]", "Zapewne,", "Przysłówek - przecinek."),
    ("Prawdopodobnie [?]", "Prawdopodobnie,", "Przysłówek - przecinek."),
    ("Być może [?]", "Być może,", "Wyrażenie - przecinek."),
    ("W związku z tym [?]", "W związku z tym,", "Wyrażenie - przecinek."),
    ("Dlatego też [?]", "Dlatego też,", "Wyrażenie - przecinek."),
    ("Wobec tego [?]", "Wobec tego,", "Wyrażenie - przecinek."),
]

for i, (front, back, rule) in enumerate(rozpr_data, start=261):
    additional_cards.append(f'    {{id: {i}, category: "Rozprawka", front: "{front}", back: "{back}", rule: "{rule}"}},\n')

# === OPOWIADANIE (10 cards) ===
opow_data = [
    ("Ni__st__d ni zow__d", "Ni stąd, ni zowąd", "Wyrażenie frazeologiczne."),
    ("Wtem / W tym", "Wtem", "'Wtem' = nagle."),
    ("Nagle [?] drzwi się otworzyły.", "Nagle drzwi się otworzyły.", "'Nagle' na początku - bez przecinka."),
    ("Niespodziewanie [?]", "Niespodziewanie,", "Przysłówek - przecinek."),
    ("Znienacka [?]", "Znienacka,", "Przysłówek - przecinek."),
    ("Raptem [?]", "Raptem,", "Przysłówek - przecinek."),
    ("Ni__chcący", "Niechcący", "Przysłówek."),
    ("Ni__umyślnie", "Nieumyślnie", "Przysłówek."),
    ("Nag__e", "Nagłe", "Przymiotnik."),
    ("W__tem", "Wtem", "Przysłówek."),
]

for i, (front, back, rule) in enumerate(opow_data, start=281):
    additional_cards.append(f'    {{id: {i}, category: "Opowiadanie", front: "{front}", back: "{back}", rule: "{rule}"}},\n')

# === WIELKA LITERA (10 cards) ===
wielka_data = [
    ("uniwersytet / Uniwersytet Warszawski", "Uniwersytet Warszawski", "Nazwy własne instytucji - wielka."),
    ("Wisła", "Wisła", "Nazwy geograficzne - wielka."),
    ("polska / Polska", "Polska", "Nazwy państw - wielka."),
    ("warszawa / Warszawa", "Warszawa", "Nazwy miast - wielka."),
    ("Kraków", "Kraków", "Nazwy miast - wielka."),
    ("Tatry", "Tatry", "Nazwy gór - wielka."),
    ("Bałtyk", "Bałtyk", "Nazwy mórz - wielka."),
    ("Europa", "Europa", "Nazwy kontynentów - wielka."),
    ("Ziemia (planeta)", "Ziemia", "Nazwy planet - wielka."),
    ("Poznań", "Poznań", "Nazwy miast - wielka."),
]

for i, (front, back, rule) in enumerate(wielka_data, start=291):
    # Remove comma from last item
    if i == 300:
        additional_cards.append(f'    {{id: {i}, category: "Wielka litera", front: "{front}", back: "{back}", rule: "{rule}"}}\n')
    else:
        additional_cards.append(f'    {{id: {i}, category: "Wielka litera", front: "{front}", back: "{back}", rule: "{rule}"}},\n')

# Write final file
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)
    f.write('\n    // === ORTOGRAFIA ch/h (40 cards) ===\n')
    for card in additional_cards[:40]:
        f.write(card)
    f.write('\n    // === PISOWNIA NIE (40 cards) ===\n')
    for card in additional_cards[40:80]:
        f.write(card)
    f.write('\n    // === ROZPRAWKA (20 cards) ===\n')
    for card in additional_cards[80:100]:
        f.write(card)
    f.write('\n    // === OPOWIADANIE (10 cards) ===\n')
    for card in additional_cards[100:110]:
        f.write(card)
    f.write('\n    // === WIELKA LITERA (10 cards) ===\n')
    for card in additional_cards[110:]:
        f.write(card)
    f.write('];\n\n')
    f.write("if (typeof module !== 'undefined') {\n")
    f.write("    module.exports = flashcards;\n")
    f.write("}\n")

print("Generated 300 flashcards successfully!")
