"""Convert PRIVACY_POLICY_{AR,EN}.md into styled standalone HTML for GitHub Pages."""
import markdown
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent

LANGS = [
    {
        "code": "ar",
        "dir": "rtl",
        "src": PROJECT_ROOT / "PRIVACY_POLICY_AR.md",
        "out": ROOT / "ar.html",
        "title": "سياسة الخصوصية | بَصيرة",
        "back_label": "العودة إلى الصفحة الرئيسية",
        "switch_label": "English",
        "switch_href": "./en.html",
    },
    {
        "code": "en",
        "dir": "ltr",
        "src": PROJECT_ROOT / "PRIVACY_POLICY_EN.md",
        "out": ROOT / "en.html",
        "title": "Privacy Policy | Basira",
        "back_label": "Back to home",
        "switch_label": "العربية",
        "switch_href": "./ar.html",
    },
]

CSS = """
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Tahoma, sans-serif;
    background: #FDF8F0;
    color: #1C1B1F;
    line-height: 1.7;
}
.container {
    max-width: 820px;
    margin: 0 auto;
    padding: 32px 24px 64px;
}
.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    padding: 16px 0;
    border-bottom: 1px solid rgba(93, 64, 55, 0.15);
}
.topbar a {
    color: #5D4037;
    text-decoration: none;
    font-weight: 600;
    padding: 8px 14px;
    border-radius: 10px;
    background: #FAF3E8;
    font-size: 14px;
}
.topbar a:hover { background: #D4A853; color: #fff; }
.brand { color: #D4A853; font-weight: 700; font-size: 20px; }
h1 { color: #5D4037; font-size: 28px; margin-top: 32px; }
h2 { color: #5D4037; font-size: 22px; margin-top: 40px; padding-bottom: 8px; border-bottom: 2px solid #D4A853; }
h3 { color: #5D4037; font-size: 18px; margin-top: 28px; }
h4 { color: #8B6B61; font-size: 16px; margin-top: 20px; }
a { color: #D4A853; }
strong { color: #5D4037; }
code {
    background: #FAF3E8;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.9em;
    color: #5D4037;
}
hr { border: 0; border-top: 1px solid rgba(93, 64, 55, 0.15); margin: 32px 0; }
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 14px;
}
th, td {
    padding: 10px 12px;
    text-align: start;
    border-bottom: 1px solid rgba(93, 64, 55, 0.12);
}
th {
    background: #FAF3E8;
    color: #5D4037;
    font-weight: 600;
}
ul { padding-inline-start: 24px; }
li { margin-bottom: 6px; }
blockquote {
    border-inline-start: 4px solid #D4A853;
    margin: 16px 0;
    padding: 8px 16px;
    background: #FAF3E8;
    border-radius: 8px;
}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="{code}" dir="{dir}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index,follow">
    <title>{title}</title>
    <style>{css}</style>
</head>
<body>
    <div class="container">
        <header class="topbar">
            <a href="./" class="brand">بَصيرة · Basira</a>
            <a href="{switch_href}">{switch_label}</a>
        </header>
        <article>
{body}
        </article>
    </div>
</body>
</html>
"""


def build():
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"])
    for lang in LANGS:
        src_text = lang["src"].read_text(encoding="utf-8")
        md.reset()
        body = md.convert(src_text)
        html = TEMPLATE.format(
            code=lang["code"],
            dir=lang["dir"],
            title=lang["title"],
            css=CSS,
            switch_href=lang["switch_href"],
            switch_label=lang["switch_label"],
            body=body,
        )
        lang["out"].write_text(html, encoding="utf-8")
        print(f"Wrote {lang['out'].relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    build()
