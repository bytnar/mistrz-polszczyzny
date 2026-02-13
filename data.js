const flashcards = [
    // === INTERPUNKCJA - Przecinek przed spójnikami ===
    {
        id: 1,
        category: "Interpunkcja",
        front: "Warto zauważyć [?] że...",
        back: "Warto zauważyć, że...",
        rule: "Przed 'że' wprowadzającym zdanie podrzędne zawsze stawiamy przecinek."
    },
    {
        id: 2,
        category: "Interpunkcja",
        front: "Mimo [?] że padało, poszliśmy.",
        back: "Mimo że padało, poszliśmy.",
        rule: "W 'mimo że' przecinek stawiamy PRZED całym wyrażeniem, nie w środku (cofanie przecinka)."
    },
    {
        id: 3,
        category: "Interpunkcja",
        front: "Nie poszedłem [?] ponieważ byłem chory.",
        back: "Nie poszedłem, ponieważ byłem chory.",
        rule: "Przed 'ponieważ' zawsze stawiamy przecinek."
    },
    {
        id: 4,
        category: "Interpunkcja",
        front: "Przyjdę [?] chyba że będzie padać.",
        back: "Przyjdę, chyba że będzie padać.",
        rule: "Przed 'chyba że' stawiamy przecinek (cofanie - przed całym wyrażeniem)."
    },
    {
        id: 5,
        category: "Interpunkcja",
        front: "Zrobię to [?] tylko że nie dzisiaj.",
        back: "Zrobię to, tylko że nie dzisiaj.",
        rule: "Przed 'tylko że' stawiamy przecinek (spójnik złożony)."
    },

    // === ORTOGRAFIA - ó/u ===
    {
        id: 6,
        category: "Ortografia ó/u",
        front: "St_ł (mebel)",
        back: "Stół",
        rule: "Ó wymienia się na O (stół → stołu, stoliki)."
    },
    {
        id: 7,
        category: "Ortografia ó/u",
        front: "W_z (pojazd)",
        back: "Wóz",
        rule: "Ó wymienia się na O (wóz → wozu, wozić)."
    },
    {
        id: 8,
        category: "Ortografia ó/u",
        front: "Pióro / pi_rko",
        back: "Piórko",
        rule: "Ó wymienia się na O (pióro → piórko)."
    },
    {
        id: 9,
        category: "Ortografia ó/u",
        front: "Drórka / dr_żka (ścieżka)",
        back: "Dróżka",
        rule: "Ó wymienia się na O (dróżka → droga)."
    },
    {
        id: 10,
        category: "Ortografia ó/u",
        front: "B_t (obuwie)",
        back: "But",
        rule: "U - brak wymiany na O (but → buta, buty)."
    },

    // === ORTOGRAFIA - rz/ż ===
    {
        id: 11,
        category: "Ortografia rz/ż",
        front: "P_zygoda",
        back: "Przygoda",
        rule: "Po P piszemy RZ (wyjątki: pszczoła, pszczelarstwo)."
    },
    {
        id: 12,
        category: "Ortografia rz/ż",
        front: "Dob_ze",
        back: "Dobrze",
        rule: "Po B piszemy RZ."
    },
    {
        id: 13,
        category: "Ortografia rz/ż",
        front: "_zeka (Wisła)",
        back: "Rzeka",
        rule: "RZ wymienia się na R (rzeka → rzeczny, rzeczka)."
    },
    {
        id: 14,
        category: "Ortografia rz/ż",
        front: "Ksią_ka",
        back: "Książka",
        rule: "Ż wymienia się na G (książka → księgi)."
    },
    {
        id: 15,
        category: "Ortografia rz/ż",
        front: "In_ynier",
        back: "Inżynier",
        rule: "Po N piszemy Ż (nie RZ)."
    },

    // === ORTOGRAFIA - ch/h ===
    {
        id: 16,
        category: "Ortografia ch/h",
        front: "Mu_a (owad)",
        back: "Mucha",
        rule: "CH wymienia się na SZ (mucha → muszka)."
    },
    {
        id: 17,
        category: "Ortografia ch/h",
        front: "Suc_y",
        back: "Suchy",
        rule: "CH wymienia się na SZ (suchy → susza)."
    },
    {
        id: 18,
        category: "Ortografia ch/h",
        front: "Bo_ater",
        back: "Bohater",
        rule: "H w wyrazach obcego pochodzenia (grecki 'heros')."
    },
    {
        id: 19,
        category: "Ortografia ch/h",
        front: "_istoria",
        back: "Historia",
        rule: "H w wyrazach obcego pochodzenia."
    },

    // === PISOWNIA NIE ===
    {
        id: 20,
        category: "Pisownia 'nie'",
        front: "__ie wiem",
        back: "Nie wiem",
        rule: "Nie z czasownikami piszemy ZAWSZE osobno."
    },
    {
        id: 21,
        category: "Pisownia 'nie'",
        front: "__ie rozumiem",
        back: "Nie rozumiem",
        rule: "Nie z czasownikami piszemy osobno (błąd: 'nierozumiem')."
    },
    {
        id: 22,
        category: "Pisownia 'nie'",
        front: "__ieładny (brzydki)",
        back: "Nieładny",
        rule: "Nie z przymiotnikami w stopniu równym piszemy łącznie."
    },
    {
        id: 23,
        category: "Pisownia 'nie'",
        front: "__ie lepszy",
        back: "Nie lepszy",
        rule: "Nie z przymiotnikami w stopniu wyższym/najwyższym piszemy OSOBNO."
    },
    {
        id: 24,
        category: "Pisownia 'nie'",
        front: "__ieład (bałagan)",
        back: "Nieład",
        rule: "Nie z rzeczownikami piszemy łącznie."
    },
    {
        id: 25,
        category: "Pisownia 'nie'",
        front: "To __ie sztuka.",
        back: "To nie sztuka.",
        rule: "Nie z rzeczownikiem jako orzecznik - piszemy osobno."
    },

    // === ROZPRAWKA - Zwroty ===
    {
        id: 26,
        category: "Rozprawka",
        front: "Moim zdan__em",
        back: "Moim zdaniem",
        rule: "Wyrażenie opinii. Nie oddzielamy przecinkiem (chyba że wtrącenie)."
    },
    {
        id: 27,
        category: "Rozprawka",
        front: "W _ogóle",
        back: "W ogóle",
        rule: "Pisownia rozdzielna! (Częsty błąd: 'wogóle')."
    },
    {
        id: 28,
        category: "Rozprawka",
        front: "Na pe__no",
        back: "Na pewno",
        rule: "Pisownia rozdzielna (podobnie: na nowo, na darmo)."
    },
    {
        id: 29,
        category: "Rozprawka",
        front: "Konkluduj__c [?]",
        back: "Konkludując,",
        rule: "Imiesłów przysłówkowy (-ąc). Oddzielamy przecinkiem."
    },
    {
        id: 30,
        category: "Rozprawka",
        front: "Nale__y podkreślić",
        back: "Należy podkreślić",
        rule: "Czasownik 'należy' (ż, nie rz)."
    },

    // === OPOWIADANIE ===
    {
        id: 31,
        category: "Opowiadanie",
        front: "Ni__st__d ni zow__d",
        back: "Ni stąd, ni zowąd",
        rule: "Wyrażenie frazeologiczne. Pisownia rozdzielna, przecinek w środku."
    },
    {
        id: 32,
        category: "Opowiadanie",
        front: "Wtem / W tym (nagle)",
        back: "Wtem",
        rule: "'Wtem' to przysłówek (nagle). 'W tym' to zaimek."
    },
    {
        id: 33,
        category: "Opowiadanie",
        front: "Nagle [?] drzwi się otworzyły.",
        back: "Nagle drzwi się otworzyły.",
        rule: "Na początku zdania 'Nagle' nie oddzielamy przecinkiem."
    },

    // === WIELKA LITERA ===
    {
        id: 34,
        category: "Wielka litera",
        front: "uniwersytet / Uniwersytet Warszawski",
        back: "Uniwersytet Warszawski",
        rule: "Nazwy własne instytucji piszemy wielką literą (błąd: 'uniwersytet Warszawski')."
    },
    {
        id: 35,
        category: "Wielka litera",
        front: "Wisła (rzeka)",
        back: "Wisła",
        rule: "Nazwy geograficzne - wielka litera."
    }
];

if (typeof module !== 'undefined') {
    module.exports = flashcards;
}
