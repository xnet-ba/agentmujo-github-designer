# AgentMujoGitHubDesigner

OpenCode skill koji dizajnira, odrzava i unapredjuje GitHub profile i repo README-e.

## Sta radi

- **Audit:** inventura repoa, curl provjera svakog widgeta/bedza, struktura README-a, media i CI rupe.
- **Dizajn:** 12 stilova iz `awesome-github-profile-gallery` + sabloni iz `awesome-github-profile-readme-templates` + provjereni matrix house style.
- **Implementacija:** profil repo, snake workflow, header/footer rollout, restrukturiranje sadrzaja.
- **Verifikacija:** raw/API provjere + idempotencija (rerun = samo SKIP).

## Instalacija

```bash
git clone https://github.com/xnet-ba/agentmujo-github-designer ~/.config/opencode/skills/agentmujo-github-designer
```

## Upotreba

Pozovi sa **`AgentMujoGitHubDesigner`** — npr. "sredi mi profil", "dodaj header na sve repove", "popravi pokvarene bedzeve".

```bash
# header/footer na sve public repove orga (default xnet-ba)
GITHUB_ORG=moj-org python scripts/apply-headers.py

# sadrzajna unapredjenja (TOC, fenceovi, details, demo, bedzevi)
python scripts/upgrade-content.py
```

## Struktura

- `SKILL.md` — skill: faze 0-4, pravila, verifikacija
- `references/techniques.md` — 12 stilova + obrasci + tabela pouzdanosti widgeta
- `references/constraints.md` — sta prezivljava GitHub renderer
- `assets/` — header.svg, divider.svg, terminal.svg, ecosystem.svg (SMIL, self-contained)
- `templates/` — PROFILE_README.template.md, REPO_HEADER_SNIPPET.md, snake.yml
- `scripts/` — apply-headers.py, upgrade-content.py

## Licenca

MIT — vidi [LICENSE](LICENSE).
