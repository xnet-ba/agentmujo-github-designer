# Sigurnosni opseg

Ovaj skill mijenja iskljucivo prezentacijski sloj (README, SVG, workflow).
Ne cita tajne, ne trazi credentiale, ne izvrsava tudji kod.

- Skripte rade `git push` i `gh api` iskljucivo s korisnikovom postojecom
  `gh` autentikacijom; ne cuvaju i ne ispisuju tokene.
- Testovi (`tests/`) ne pristupaju mrezi — live URL provjere se rade rucno
  curl-om (SKILL.md, Faza 1 i Faza 4).
- Prijavljene ranjivosti: otvoriti issue na
  https://github.com/xnet-ba/agentmujo-github-designer/issues
