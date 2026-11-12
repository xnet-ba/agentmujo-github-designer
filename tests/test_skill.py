"""Static validation for agentmujo-github-designer: assets, templates, skill contract.
No network access — live URL checks stay manual (SKILL.md Faza 1/4).
Run: python -m pytest tests/ -q
"""
import py_compile
import re
import xml.dom.minidom
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_scripts_compile():
    for name in ("apply-headers.py", "upgrade-content.py", "maintain.sh"):
        p = ROOT / "scripts" / name
        assert p.exists(), f"nedostaje scripts/{name}"
    for name in ("apply-headers.py", "upgrade-content.py"):
        py_compile.compile(str(ROOT / "scripts" / name), doraise=True)


def test_maintain_is_shell():
    first = (ROOT / "scripts" / "maintain.sh").read_text(encoding="utf-8").split("\n")[0]
    assert first.startswith("#!/bin/bash")


def test_svg_assets_self_contained():
    for name in ("header.svg", "divider.svg", "terminal.svg", "ecosystem.svg"):
        p = ROOT / "assets" / name
        assert p.exists(), f"nedostaje assets/{name}"
        xml.dom.minidom.parse(str(p))  # mora biti validan XML
        txt = p.read_text(encoding="utf-8")
        assert "<script" not in txt and "onclick" not in txt and "onload" not in txt
        assert "<animate" in txt, f"{name} nema SMIL animaciju"
        if name == "header.svg":
            assert "textLength" in txt  # wordmark raspored ne smije puci


def test_snake_workflow_template():
    t = (ROOT / "templates" / "snake.yml").read_text(encoding="utf-8")
    assert "Platane/snk" in t
    assert "target_branch" in t and "output" in t
    assert "snake-dark" in t and "snake-light" in t  # dark/light varijante


def test_skill_frontmatter():
    head = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---")
    assert len(head) >= 3 and "name:" in head[1] and "description:" in head[1]
    assert "tools:" in head[1]


def test_profile_template_placeholders():
    t = (ROOT / "templates" / "PROFILE_README.template.md").read_text(encoding="utf-8")
    for ph in ("{{USER}}", "{{TAGLINE}}", "{{TYPING_LINES}}", "{{YAML_BLOCK}}",
               "{{FLAGSHIP_TABLE}}", "{{ACCENT}}", "snake-dark", "snake-light"):
        assert ph in t, f"nedostaje placeholder {ph}"
    assert "TODO" not in t and "FIXME" not in t


def test_repo_snippet_marker():
    t = (ROOT / "templates" / "REPO_HEADER_SNIPPET.md").read_text(encoding="utf-8")
    assert "xnet-ba-matrix-header-v1" in t and "REPO-NAME" in t


def test_references_coverage():
    tech = (ROOT / "references" / "techniques.md").read_text(encoding="utf-8")
    for term in ("fieldset", "kbd", "devicons", "herokuapp", "402", "DenverCoder1", "AlexMartinFR"):
        assert term in tech, f"techniques.md: nedostaje {term}"
    cons = (ROOT / "references" / "constraints.md").read_text(encoding="utf-8")
    for term in ("SMIL", "camo", "textLength", "<picture>", "<details>"):
        assert term in cons, f"constraints.md: nedostaje {term}"
    assert (ROOT / "references" / "examples" / "DenverCoder1.md").exists()
    assert (ROOT / "references" / "examples" / "AlexMartinFR.md").exists()


def test_no_secrets_in_repo():
    bad = re.compile(r"ghp_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY")
    for p in ROOT.rglob("*"):
        if ".git/" in str(p) or p.is_dir() or p.suffix in (".svg", ".png"):
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        assert not bad.search(txt), f"tajna u {p}"
