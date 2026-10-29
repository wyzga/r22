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
- Pojemność 33 335 miejsc (bez 118 stanowisk trybuny prasowej); liczby miejsc w sektorach według systemu biletowego.
- Symulator zajętości: suwak „Zajętość” zapełnia stadion od środków trybun, narożniki na końcu.
