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

- `stadion-wisla/tex/` – tekstury (murawa 4K, beton, elewacja, poszycie dachu, park, krzesełko).
- `stadion-wisla/herb.svg` – herb klubu.

## Model

- Trybuny A (z H), C, E, G i narożniki B, D, F; pawilon medialny w narożniku H.
- Liczby rzędów jak na stadionie: G i C po 32, poziomy dolne 18, górne: A/H 21, E 25, narożniki B/D/F 24.
- Model buduje 32 186 miejsc (bez 118 stanowisk trybuny prasowej); przy każdym wyjściu po 2 miejsca z boku zostają wolne na przejście. Rząd na trybunie E ma 253 miejsca (dół: E11 1–47, E12 48–96, …), H11 ma 47 w rzędzie, numeracja w rzędzie biegnie dalej przez sektory (E, G, C, narożniki). Sektory E i H11 są policzone z długości rzędów, więc mają więcej miejsc niż w systemie biletowym; G, C oraz ADM i A11 mieszczą mniej; pozostałe sektory zgadzają się z systemem biletowym.
- Symulator zajętości: suwak „Zajętość” zapełnia stadion od środków trybun, narożniki na końcu.
