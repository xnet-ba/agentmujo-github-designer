<!-- xnet-ba-matrix-header-v1 -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00FF41&height=140&section=header&text=agentmujo-github-designer&fontColor=000000&fontSize=24&fontAlignY=32&desc=open-source%20AI%20iz%20BiH&descAlignY=55" width="100%" alt="agentmujo-github-designer"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=2800&pause=800&color=00FF41&center=true&vCenter=true&width=700&lines=xnet-ba+%3A%3A+open-source+AI+iz+BiH;citaj+README+pa+pokreni;PR+dobrodosli)](https://github.com/xnet-ba/agentmujo-github-designer)

[![Stars](https://img.shields.io/github/stars/xnet-ba/agentmujo-github-designer?style=flat-square&color=00FF41&labelColor=000000)](https://github.com/xnet-ba/agentmujo-github-designer/stargazers)
[![License](https://img.shields.io/github/license/xnet-ba/agentmujo-github-designer?style=flat-square&color=00FF41&labelColor=000000)](LICENSE)
[![Top lang](https://img.shields.io/github/languages/top/xnet-ba/agentmujo-github-designer?style=flat-square&color=00FF41&labelColor=000000)](https://github.com/xnet-ba/agentmujo-github-designer)
[![Last commit](https://img.shields.io/github/last-commit/xnet-ba/agentmujo-github-designer?style=flat-square&color=00FF41&labelColor=000000)](https://github.com/xnet-ba/agentmujo-github-designer/commits)
[![matrix](https://img.shields.io/badge/MATRIX-xnet--ba-00FF41?style=flat-square&labelColor=000000)](https://github.com/xnet-ba)

</div>

---
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

---

<div align="center">
<img src="https://raw.githubusercontent.com/xnet-ba/xnet-ba/main/assets/divider.svg" width="100%" alt=""/>
<sup>part of <a href="https://github.com/xnet-ba">xnet-ba matrix</a> — open-source AI iz BiH</sup>
</div>
