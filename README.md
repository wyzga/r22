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

- `stadion-wisla/tex/` – tekstury (murawa 4K, poszycie dachu, park); beton i niebo są generowane w kodzie.
- `stadion-wisla/herb.svg` – herb klubu.

## Model

- Trybuny A (z H), C, E, G i narożniki B, D, F; pawilon medialny w narożniku H. Jego szklany bęben ma 10 m promienia, a betonowy cokół dochodzi do końca skrzydła H11. Górna krawędź cokołu ma barierki: z przodu i wzdłuż boków przy G i H11, dopóki te trybuny są niższe od cokołu. Skrzydło kończy się tuż za ostatnimi krzesełkami, bez pustych stopni. H11 jest niebieski we wszystkich rzędach od środka wejścia (schodów z murawy) do końca skrzydła.
- Każde krzesełko pochodzi z planu miejsc klubu, z prawdziwym sektorem, rzędem i numerem: 32 320 na trybunach i 938 na balkonie przed skyboxami między poziomami (skyboxy SK01–SK34 po 4 rzędy, loża prezydencka, balkony na E), razem 33 258. Z 241 stanowiskami trybuny prasowej to 33 499, tyle co w planie.
- Liczby rzędów jak w planie: G 32, C 33, poziomy dolne 18 (narożniki D i F 22), górne: A/H 21, E 25, narożniki B/D/F 25.
- Schody, wyjścia, tunel dla piłkarzy i trybuna prasowa są tam, gdzie plan zostawia przerwy w rzędach: 2–5 brakujących miejsc to schody, większa przerwa przez co najmniej trzy rzędy to wyjście.
- Tam, gdzie schody dolnego poziomu (na C i G jedynego) dochodzą do pierwszego rzędu, są zejścia na murawę, jak na zdjęciu E14: kilka stopni przed ścianą, barierki po obu stronach i niska (1 m) żółta bramka z poprzeczką i tablicą „Wyjście ewakuacyjne” z nazwą sektora. Takie zejścia mają też wyjścia narożników. Na C i G przed pierwszym rzędem biegnie szklana barierka, przerwana tylko przy bramkach.
- Wyjście jest węższe niż przerwa w planie: po obu stronach, za barierkami, biegną w górę sektora schody szerokie na trzy krzesełka (na G i C na dwa, jak na zdjęciu G3).
- Trybuny za bramkami są szerokie jak w planie: C ma 80 m, G 73,5 m (od strony pawilonu kończy się wcześniej). Między G3 a G4, przy sektorze gości, biegną od pierwszego do ostatniego rzędu schody szerokie na trzy krzesełka, z szarego betonu (pozostałe schody na G są żółte), z barierkami po obu stronach, jak na zdjęciu. Plan nie ma tam przerwy, więc krzesełka całej trybuny są ustawione nieco ciaśniej.
- W narożnikach B, D i F obok trybuny za bramką jest przejazd dla karetek na poziomie murawy (4,5 m od końca tej trybuny), przez budynek narożnika na zewnątrz. Za dolnym poziomem to prostokątny tunel wysoki jak ten poziom: nad nim chodnik i pas skyboxów biegną dalej aż do trybuny za bramką. Górny poziom narożnika kończy się od strony trybuny za bramką prostą krawędzią, tuż za najdalszym krzesełkiem. Rzędy, które kończą się wcześniej, dochodzą do niej gołym betonem, bez wcięcia. Wyjątkiem są najwyższe rzędy, coraz krótsze: tam poziom jest ścięty tuż za ostatnim krzesełkiem każdego rzędu i rzędów nad nim, bez betonu w rogu. Budynek narożnika kończy się na wysokości ostatniego rzędu, więc nad krzesełkami nie stoi żadna ściana. Ściana dolnego poziomu przy przejeździe ma barierki. Dolny poziom narożnika ma wyjście na tej samej wysokości co wyjścia dolnego poziomu sąsiedniej trybuny bocznej (E przy D i F, A przy B). Stoi w części biegnącej wzdłuż tej trybuny, pośrodku pustych stopni, które plan zostawia w pierwszych rzędach. Od wyjścia schody prowadzą prosto w dół, przez te rzędy, do murawy. Pierwsze rzędy G i C, krótsze w planie o ok. 4 m na końcach, są tam ścięte, a przy przejazdach pozostałe rzędy tego końca wiszą 5,5 m nad ziemią, więc przejazd ma pod nimi prześwit na wylot. Boki G i C, otwarty koniec górnego poziomu narożników przy trybunie za bramką, krawędź obu poziomów H przy pawilonie medialnym oraz przód i końce balkonów skyboxów na A z H, B i E mają barierki ze szklanym wypełnieniem.
- Narożniki wypełniają kwadrat między trybuną boczną a trybuną za bramką: rzędy biegną dalej wzdłuż trybuny bocznej, skręcają o 45° w przekątną i jeszcze raz wzdłuż trybuny za bramką, a bloki dzielą schody i wyjścia. Tam, gdzie plan nie ma krzesełek na końcach rzędów (wejście z przodu dolnego poziomu, przejście w górnym), są schody: na dolnym poziomie odgrodzone barierkami, na górnym bez nich. Na górnym poziomie, w części wzdłuż trybuny bocznej, wyjście jest pośrodku sektora za załamaniem (B22, D24, F22). Przerwa między tym sektorem a sąsiednim bliżej załamania jest zwykłymi schodami, tak szerokimi jak wyżej.
- Dachy trybun za bramkami (C i G) kończą się tam, gdzie krzesełka, tuż za końcami trybun.
- Nad ostatnim rzędem E nie ma szkła: dach leży na grubej betonowej belce, a ta na rzędzie betonowych słupów co ok. 4,4 m, jak na zdjęciu. Między słupami jest prześwit: budynek za trybuną kończy się na wysokości barierki za ostatnim rzędem, więc widać przez nie niebo. Belka i słupy biegną dalej pod dachem nad narożnikami D i F.
- Czoła górnych poziomów (trybuny boczne i narożniki) to goły beton, bez reklam. Reklamy zostały tylko na bandach przy murawie.
- Bez elewacji: z zewnątrz budynki trybun są gładkie i ciemne, bez białych pasów, napisów i tekstury. Cały beton (trybuny, schody, słupy i belki, czoła poziomów, cokoły, ziemianki, plac i chodniki) ma jedną nową, jasnoszarą teksturę lanego betonu. Ma miękkie, nieregularne przebarwienia, drobne ziarno i małe pory po pęcherzykach powietrza. Tekstura jest generowana w przeglądarce, bez osobnego pliku, i powtarza się bez widocznych szwów.
- Na górze A z H, nad ostatnimi rzędami, na obu końcach stoją przeszklone kabiny komentatorów. Ich przednie szyby są nachylone o 15° w stronę boiska, a górą chowają się pod betonowym okapem. Między kabinami, na tej samej wysokości, biegnie galeria, jak na zdjęciu. Z przodu ma szklaną barierkę, z tyłu szklaną ścianę w ciemnych ramach między jasnymi betonowymi słupami. Na galerii stoją miejsca dla obsługi: dwa rzędy niebieskich krzesełek na stopniu, w dwóch odcinkach po obu stronach środka (nad trybuną prasową ich nie ma).
- Między górnymi poziomami trybun bocznych a narożnikami (A23 i B22, E i D, E i F) biegną schody. Po obu ich stronach, przez całą długość od pierwszego do ostatniego rzędu, stoją szklane barierki.
- Na C i G, tam gdzie krzesełka dwóch sąsiednich sektorów stykają się bez schodów (C1–C5, G1/G2, G2/G3, G4/G5), między skrajnymi krzesełkami biegnie szklana barierka od pierwszego do ostatniego rzędu, jak na zdjęciu. Ma turkusowe słupki i poręcz oraz ukośną ciemnoniebieską belkę wzdłuż krawędzi rzędów. Krzesełka zostały na swoich miejscach, barierka mieści się w wąskiej przerwie między nimi. Przy sektorze gości (G3/G4) zostały schody z własnymi barierkami.
- Na środku C, na dole, dokładnie za środkiem bramki, stoi „gniazdo” gniazdowego, jak na zdjęciu. To czerwona stalowa konstrukcja na czterech kwadratowych słupach postawionych na stopniach pierwszych rzędów. Ma pomost ok. 2,2 m nad pierwszym rzędem z barierką dookoła, drabinkę z boku i ramę odchyloną do tyłu nad rzędy za nim.
- Dach C i G niosą okrągłe niebieskie stalowe słupy przed czarną szklaną ścianą z tyłu trybuny, jak na zdjęciu. Stoją dokładnie tam, gdzie stykają się sektory (także przy sektorze gości), oraz na obu końcach trybuny. Z ich szczytów biegną odciągi do dachu.
- Jasne pasy na przedniej krawędzi dachów są odchylone o 15° do góry: ich góra cofa się od boiska, więc patrzą lekko w niebo.
- Pod dachami wiszą na prętach czarne głośniki, równo rozłożone wzdłuż trybuny: po 8 na A i E, po 5 na C i G.
- Telebimy pod dachami trybun bocznych mają 6 m wysokości (8 × 6 m, format 4:3).
- Plan jest schematyczny. Na prostych trybunach siatka miejsc jest rozciągnięta na długość trybuny. Na trybunie głównej wszystkie poziomy są wyrównane tak, żeby tunel dla piłkarzy wypadał dokładnie na linii środkowej. Na E oraz na A z H, na obu poziomach, jak na zdjęciach, nie ma schodów między sektorami (przerwy z planu są zamknięte), tylko przez środki sektorów. Tam, gdzie w rzędzie planu brakuje jednego miejsca (A22/A21 i VIP Royal/H22 w rzędach 14–21), krzesełka też dochodzą do siebie, bez pustej kolumny. Na E bloki między nimi niosą napisy WISŁA (górny poziom) i 1906 (dolny). W narożnikach każde miejsce zachowuje swoje położenie na długości swojego załamanego rzędu.
- Krzesełka mają prostokątne siedziska i oparcia z prostymi rogami. Ciemniejsza krawędź jest tylko na płaskich powierzchniach, boki są gładkie.
- Przed trybuną główną są wpuszczone w murawę ławki: po obu stronach tunelu 3-osobowe ławki sędziów, dalej 12-osobowe ławki rezerwowych, wszystkie pod przezroczystym daszkiem.
- Etykiety sektorów wyglądają jak tablice na stadionie (zdjęcie E14): litera trybuny biała na czerwonym polu, numer biały na niebieskim. Sektory z nazwą (VIP, prasa) mają jedno niebieskie pole.
- Po najechaniu myszką na sektor jego etykieta ożywa. Podskakuje co ok. 0,6 s, przy lądowaniu lekko się spłaszcza, a przy wybiciu wydłuża. Do tego jest nieco większa i pulsuje jaśniej. Gdy kursor zjedzie z sektora, etykieta płynnie wraca na swoje miejsce.
- Na niebie są delikatne, rzadkie chmurki pogodowe. Przy horyzoncie się przerzedzają, a w nocy ciemnieją i prawie znikają. W nocy na niebie świecą gwiazdy o różnej jasności i księżyc w pełni z ciemniejszymi morzami i delikatną poświatą. Chmury przesłaniają gwiazdy i księżyc, a te w pobliżu księżyca są przez niego podświetlone.
- Przycisk „Noc” przełącza na widok nocny: ciemne niebo i włączone reflektory. Głowice na 10 masztach świecą i każda rzuca snop światła na murawę. Pod dachami, nad ostatnimi rzędami, świecą lampy (co ok. 6 m), więc górne części trybun też są widoczne. Światło jest ciepłobiałe, a murawa zostaje zielona.
- Na środku C i G, na samej górze, nie ma wyjścia, tylko stanowisko kamery: płaski podest z barierką z przodu i po bokach, bez drzwi.
- Przed trybunami za bramkami (C i G) wisi na całej ich szerokości siatka za bramką, wysoka na 2,5 wysokości bramki (6,1 m), z tej samej siatki co bramki, rozpięta między cienkimi ciemnymi słupkami co ok. 12 m.
- Symulator zajętości: suwak „Zajętość” zapełnia stadion od środków trybun, narożniki na końcu. Każdy kibic ma głowę w kolorze skóry i czarne włosy. Na C (trybuna gospodarzy) 9 na 10 kibiców jest ubranych na czerwono, tylko w przednich rzędach przy środkowych schodach, między dwoma dolnymi ramionami gwiazdy, większość jest na czarno. Co jakiś czas kibice podnoszą tam duże flagi i machają nimi na boki, jak na zdjęciu: połowa w poziome pasy czerwony–biały–niebieski–biały–czerwony, ćwierć niebiesko-biało-czerwonych, ćwierć czerwonych z białą gwiazdą na środku.
- Żadne dwie ściany modelu nie leżą w tej samej płaszczyźnie (schody, cokoły, budynki za trybunami są odsunięte o 1–2 cm), więc przy ruchu kamery powierzchnie nie migoczą. Numery na krzesełkach pokazują się dopiero z bliska, gdy da się je przeczytać; z daleka rozpadałyby się w migające białe punkty.
