# Synerise Arena Kraków 3D

Interaktywny model 3D stadionu Wisły Kraków (Stadion Miejski im. Henryka Reymana). Kliknięcie krzesełka przenosi na to miejsce i pokazuje widok na murawę. To samo robi wyszukiwarka w karcie tytułowej: wpisz sektor, rząd i miejsce (np. `E21 5 12`) albo wybierz je w pickerach i kliknij „Zobacz”. Pickery to karty z kafelkami: sektory pogrupowane według trybun i z wyszukiwaniem, rzędy i miejsca jako siatka numerów. Działa w nich klawiatura: strzałki, Enter, Esc i wpisywanie numeru. Projekt nieoficjalny.

## Uruchomienie

Otwórz `stadion-wisla/index.html` w przeglądarce. To samodzielna kopia z wbudowanymi teksturami i herbem, działa także z dysku (`file://`).

## Pliki

- `stadion-wisla/stadion.html` – źródło strony (Three.js); tekstury wczytuje z `tex/`, herb z `herb.svg`.
- `stadion-wisla/build.mjs` – buduje `index.html` ze `stadion.html`, wbudowując tekstury i herb jako `data:` URI:

  ```bash
  node stadion-wisla/build.mjs
  ```

- `stadion-wisla/data/` – plan miejsc klubu (`seats.json`, `sectors.json`) ze strony stadium.wislakrakow.com.
- `stadion-wisla/tools/seatmap.mjs` – zamienia plan miejsc na zwarty układ krzesełek i wpisuje go do `stadion.html` (blok `SEATMAP`):

  ```bash
  node stadion-wisla/tools/seatmap.mjs
  ```

- `stadion-wisla/tex/` – tekstury (murawa 4K, beton, elewacja, poszycie dachu, park).
- `stadion-wisla/herb.svg` – herb klubu.

## Model

- Trybuny A (z H), C, E, G i narożniki B, D, F; pawilon medialny w narożniku H. Jego szklany bęben ma 10 m promienia, a betonowy cokół dochodzi do końca skrzydła H11. Skrzydło kończy się tuż za ostatnimi krzesełkami, bez pustych stopni. Pierwszy rząd H11 od schodów do końca skrzydła jest niebieski.
- Każde krzesełko pochodzi z planu miejsc klubu, z prawdziwym sektorem, rzędem i numerem: 32 320 na trybunach i 938 na balkonie przed skyboxami między poziomami (skyboxy SK01–SK34 po 4 rzędy, loża prezydencka, balkony na E), razem 33 258. Z 241 stanowiskami trybuny prasowej to 33 499, tyle co w planie.
- Liczby rzędów jak w planie: G 32, C 33, poziomy dolne 18 (narożniki D i F 22), górne: A/H 21, E 25, narożniki B/D/F 25.
- Schody, wyjścia, tunel dla piłkarzy i trybuna prasowa są tam, gdzie plan zostawia przerwy w rzędach: 2–5 brakujących miejsc to schody, większa przerwa przez co najmniej trzy rzędy to wyjście.
- Tam, gdzie schody dolnego poziomu (na C i G jedynego) dochodzą do pierwszego rzędu, są zejścia na murawę, jak na zdjęciu E14: kilka stopni przed ścianą, barierki po obu stronach i niska (1 m) żółta bramka z poprzeczką i tablicą „Wyjście ewakuacyjne” z nazwą sektora. Takie zejścia mają też wyjścia narożników.
- Wyjście jest węższe niż przerwa w planie: po obu stronach, za barierkami, biegną w górę sektora schody szerokie na trzy krzesełka (na G i C na dwa, jak na zdjęciu G3).
- Trybuny za bramkami są szerokie jak w planie: C ma 80 m, G 73,5 m (od strony pawilonu kończy się wcześniej). Między G3 a G4, przy sektorze gości, biegną od pierwszego do ostatniego rzędu schody szerokie na trzy krzesełka, z szarego betonu (pozostałe schody na G są żółte), z barierkami po obu stronach, jak na zdjęciu. Plan nie ma tam przerwy, więc krzesełka całej trybuny są ustawione nieco ciaśniej.
- W narożnikach B, D i F obok trybuny za bramką jest przejazd dla karetek na poziomie murawy (4,5 m od końca tej trybuny), przez budynek narożnika na zewnątrz. Za dolnym poziomem to prostokątny tunel wysoki jak ten poziom: nad nim chodnik i pas skyboxów biegną dalej aż do trybuny za bramką. Górny poziom narożnika kończy się od strony trybuny za bramką prostą krawędzią, tuż za najdalszym krzesełkiem. Rzędy, które kończą się wcześniej, dochodzą do niej gołym betonem, bez wcięcia. Ściana dolnego poziomu przy przejeździe ma barierki. Dolny poziom narożnika ma wyjście na tej samej wysokości co wyjścia dolnego poziomu sąsiedniej trybuny bocznej (E przy D i F, A przy B). Stoi w części biegnącej wzdłuż tej trybuny, pośrodku pustych stopni, które plan zostawia w pierwszych rzędach. Od wyjścia schody prowadzą prosto w dół, przez te rzędy, do murawy. Pierwsze rzędy G i C, krótsze w planie o ok. 4 m na końcach, są tam ścięte, a przy przejazdach pozostałe rzędy tego końca wiszą 5,5 m nad ziemią, więc przejazd ma pod nimi prześwit na wylot. Boki G i C, otwarty koniec górnego poziomu narożników przy trybunie za bramką, krawędź obu poziomów H przy pawilonie medialnym oraz przód i końce balkonów skyboxów na A z H, B i E mają barierki ze szklanym wypełnieniem.
- Narożniki wypełniają kwadrat między trybuną boczną a trybuną za bramką: rzędy biegną dalej wzdłuż trybuny bocznej, skręcają o 45° w przekątną i jeszcze raz wzdłuż trybuny za bramką, a bloki dzielą schody i wyjścia. Tam, gdzie plan nie ma krzesełek na końcach rzędów (wejście z przodu dolnego poziomu, przejście w górnym), są schody: na dolnym poziomie odgrodzone barierkami, na górnym bez nich.
- Plan jest schematyczny. Na prostych trybunach siatka miejsc jest rozciągnięta na długość trybuny. Na trybunie głównej wszystkie poziomy są wyrównane tak, żeby tunel dla piłkarzy wypadał dokładnie na linii środkowej. Na E oraz na A z H, na obu poziomach, jak na zdjęciach, nie ma schodów między sektorami (przerwy z planu są zamknięte), tylko przez środki sektorów. Na E bloki między nimi niosą napisy WISŁA (górny poziom) i 1906 (dolny). W narożnikach każde miejsce zachowuje swoje położenie na długości swojego załamanego rzędu.
- Krzesełka mają prostokątne siedziska i oparcia z prostymi rogami. Ciemniejsza krawędź jest tylko na płaskich powierzchniach, boki są gładkie.
- Przed trybuną główną są wpuszczone w murawę ławki: po obu stronach tunelu 3-osobowe ławki sędziów, dalej 12-osobowe ławki rezerwowych, wszystkie pod przezroczystym daszkiem.
- Symulator zajętości: suwak „Zajętość” zapełnia stadion od środków trybun, narożniki na końcu.
