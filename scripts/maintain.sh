#!/bin/bash
# Odrzavanje GitHub prisutnosti: svjezi klonovi + header rollout + sadrzajni upgrade.
# Obje python skripte su idempotentne: gotovo se preskace (SKIP), radi samo novo.
# Pokretanje: ./scripts/maintain.sh  (preporuka: cron mjesecno)
#   0 6 1 * *  /home/sha/.config/opencode/skills/agentmujo-github-designer/scripts/maintain.sh >> /tmp/opencode/repo-headers/maintain.log 2>&1
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
rm -rf /tmp/opencode/repo-headers
python3 "$HERE/apply-headers.py"
python3 "$HERE/upgrade-content.py"
echo "[maintain] gotovo: $(date -u +%FT%TZ)"
