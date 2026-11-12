# Tehnike — iz dva kataloga + provjerena praksa

Izvori: `nitr0yukkuri/awesome-github-profile-gallery` (12 stilova, tools, FAQ)
i `durgeshsamariya/awesome-github-profile-readme-templates` (copy-paste sabloni).
Pravilo: katalog je inspiracija, ali svaki widget se provjerava curl-om (Faza 1).

## 12 stilova (galerija 1) — kada koji

- **Minimalistic** — 2-3 elementa, brz, za ozbiljne profile. Najsigurniji.
- **Descriptive** — tekst + struktura, za dokumentacijske tipove.
- **Badges/Icons** — shields/devicons/skillicons grupe, za stack-heavy profile.
- **Code** — yaml/pre blok kao licna karta (kao Nikhilesh `role/focus` blok).
- **Dynamic** — stats/streak/trophy/langs koji se sami osvjezavaju.
- **Animation** — SMIL SVG (sweep, typing, snake). Jedina animacija koja radi.
- **Interactive** — sve klikabilno + `<details>` + dark/light `<picture>`.
- **Image** — veliki banner/hero kao nosilac identiteta.
- **Game** — snake i druge contribution igre.
- **Innovative** — terminali, pipeline trake, custom SVG instrumenti.
- **Fancy Fonts** — ASCII/emoji tipografija (oprez: emoji kvari TOC anchore).
- **A Little Bit of Everything** — risks anti-pattern: samo ako profil ostane citljiv.

## Sabloni (galerija 2) — preuzeti obrasci

- `<fieldset style="border...">` + `<legend>` — uokvirene sekcije, prezivljava renderer.
- `<kbd>` grupe — Back-end / Front-end / Library / Ostalo sa devicons ikonama (30px).
- devicons CDN: `cdn.jsdelivr.net/gh/devicons/devicon@latest/...`, fallback
  `raw.githubusercontent.com/devicons/devicon/master/...`, specijalni logo
  `vectorlogo.zone`. Alternativa skillicons.dev (jedan URL za cijeli red).
- Grupisani shields po kategorijama (Languages/Frontend/Backend/Cloud/CI/IDE),
  svaki linka na zvanicnu dokumentaciju alata.
- `<img align="right" width="240">` — plutajuca slika uz tekst; giphy GIF kao akcenat.
- `<pre>` emoji bullet blok + `<hr>` separatori za ritam.
- `height="180em"` stats + langs jedan pored drugog unutar linka na profil.
- grid-snake varijanta: snake u grid okviru umjesto gole linije.

## Widgeti — pouzdanost (provjereno curl-om, nov 2026)

| Widget | URL baza | Status | Napomena |
|---|---|---|---|
| capsule-render | `capsule-render.vercel.app` | 200 OK | header/section/footer valovi |
| typing SVG | `readme-typing-svg.demolab.com` | 200 OK | NE herokuapp (mrtav domen) |
| skillicons | `skillicons.dev` | 200 OK | jedan URL po redu ikona |
| devicons | `cdn.jsdelivr.net/gh/devicons` | OK | pojedinacne ikone 30px |
| shields | `img.shields.io` | 200 OK | stars/license/lang/last-commit/followers |
| komarev | `komarev.com/ghpvc` | 200 OK | broj posjeta |
| streak | `streak-stats.demolab.com` | 200 OK | NE herokuapp (mrtav) |
| stats | `github-readme-stats.vercel.app` | FLAKY (503) | drzati, ali dizajn ne smije ovisiti o njemu |
| trophy | `github-profile-trophy.vercel.app` | LIVE na xnet-ba | tema matrix, `no-frame+no-bg` |
| snake | `Platane/snk` + `output` grana | OK | treba workflow `write` permisije |
| activity-graph | `github-readme-activity-graph` | 402 MRTAV | ne ugradjivati |
| readme-x-cards / gh-stats-card | iz tools liste galerije | NEPROVJERENO | curl prije upotrebe |

## Kucni matrix stil (default za xnet-ba)

`#00FF41` na `#020a02`/`#000000`, `visitor@matrix`, yaml licna karta,
terminal.svg (SMIL kucanje 20s petlja), ecosystem.svg traka
SKILLS→MEMORY→MODELS→APPS, divider.svg flow, snake dark/light `<picture>`,
capsule footer. Sabloni u `templates/`, gotovi SVG-ovi u `assets/`.
