# Synerise Arena Kraków 3D

Interaktywny model 3D stadionu Wisły Kraków (Stadion Miejski im. Henryka Reymana). Kliknięcie krzesełka przenosi na to miejsce i pokazuje widok na murawę. Projekt nieoficjalny.

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

- `stadion-wisla/tex/` – tekstury (murawa 4K, beton, elewacja, poszycie dachu, park, krzesełko).
- `stadion-wisla/herb.svg` – herb klubu.

## Model

- Trybuny A (z H), C, E, G i narożniki B, D, F; pawilon medialny w narożniku H.
- Każde krzesełko pochodzi z planu miejsc klubu, z prawdziwym sektorem, rzędem i numerem: 32 320 na trybunach i 938 na balkonie przed skyboxami między poziomami (skyboxy SK01–SK34 po 4 rzędy, loża prezydencka, balkony na E), razem 33 258. Z 241 stanowiskami trybuny prasowej to 33 499, tyle co w planie.
- Liczby rzędów jak w planie: G 32, C 33, poziomy dolne 18 (narożniki D i F 22), górne: A/H 21, E 25, narożniki B/D/F 25.
- Schody, wyjścia, tunel dla piłkarzy i trybuna prasowa są tam, gdzie plan zostawia przerwy w rzędach: 2–5 brakujących miejsc to schody, większa przerwa przez co najmniej trzy rzędy to wyjście.
- Plan jest schematyczny. Na prostych trybunach siatka miejsc jest rozciągnięta na długość trybuny, więc na G i C (67 m) krzesełka są węższe. W narożnikach każde miejsce zachowuje swoje położenie w szerokości wachlarza.
- Symulator zajętości: suwak „Zajętość” zapełnia stadion od środków trybun, narożniki na końcu.
