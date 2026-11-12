# GitHub rendering ogranicenja — dizajn koji prezivljava

1. **Nema JS, nema CSS.** README se renderuje kroz camo proxy kao `<img>`;
   scripting je inertan, eksterni fontovi se ne ucitavaju.
2. **Animacija = samo SMIL.** `<animate>` / `<animateTransform>` rade;
   CSS `@keyframes` ne rade pouzdano. Preferiraj SMIL za sweep, blink, flow.
3. **Tamna ploca u fajlu.** GitHub kontrolise pozadinu oko README-a — SVG mora
   sam nacrtati tamni rect, inace je necitljiv u light temi.
4. **Monospace preko `textLength`.** Font zavisi od OS-a gledaoca; fiksiraj
   raspored sa `textLength` + `lengthAdjust="spacing"`, ne pogadjaj sirinu.
5. **Dark/light:** `<picture>` + `<source media="(prefers-color-scheme: ...)">`
   + fallback `<img>`. Radi za snake, hero, stat kartice.
6. **Interaktivnost = linkovi + `<details>`.** Nema hovera, modala, tabova.
   Sve klikabilno mora biti `<a>` ili markdown link; sklopivo je `<details>`.
7. **MP4 se ne renderuje inline.** Demo video = GIF inline + link na MP4.
8. **Emoji u headingu jede TOC anchor.** Slugger brise emoji; dijakritika
   (`čćžš`) ostaje — anchor provjeri rucno ako je kritican.
9. **ASCII art samo u fenceovima.** Bez ` ``` ` GitHub kolapsira whitespace.
10. **CDN kesira.** `raw.githubusercontent` kasni minutama — svjeze stanje
    provjeri preko `gh api repos/.../contents/... --jq .content | base64 -d`.
11. **Vanjski servisi padaju.** Dizajn mora izgledati dobro i kad stats/typing
    vrate gresku: lokalni SVG nosi identitet, widgeti su bonus.
