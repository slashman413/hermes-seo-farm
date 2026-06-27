#!/usr/bin/env python3
"""
hermes-seo-farm: Auto-generate SEO-optimized content for GitHub Pages.
Template-based content generation using the user's expertise areas.
"""
import os, sys, json, random
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / "_posts"
DATA_DIR = BASE_DIR / "data"

# --- Content Templates by Expertise Area ---
CONTENT_TEMPLATES = {
    "investing": [
        {
            "title": "新手必看：台股ETF vs 個股的3個關鍵差異",
            "tags": ["ETF", "台股", "投資新手"],
            "body": [
                "## 為什麼要比較 ETF 和個股？",
                "對於剛開始投資台股的人來說，最常遇到的問題就是：該買 ETF 還是個股？",
                "## 1. 分散風險的程度不同",
                "ETF 追蹤一籃子股票，單一公司倒閉對你的影響有限。個股則是把雞蛋放在同一個籃子裡。",
                "## 2. 管理成本",
                "ETF 的管理費通常低於 0.5%，而個股投資需要你花時間研究財報、技術分析。",
                "## 3. 報酬潛力",
                "個股有機會帶來超額報酬（台積電十年漲10倍），ETF 則提供市場平均報酬。",
                "## 結論",
                "對於大多數投資人，ETF 是更好的起點。等你有足夠的知識和經驗後，再考慮個股。",
            ],
        },
        {
            "title": "定期定額 vs 單筆投入：哪個更適合台股？",
            "tags": ["定期定額", "投資策略", "台股"],
            "body": [
                "## 兩種投資方式的比較",
                "定期定額和單筆投入各有優缺點，取決於你的資金狀況和風險承受度。",
                "## 定期定額的優勢",
                "✓ 分散買入成本\n✓ 適合每月有固定收入的上班族\n✓ 心理壓力小",
                "## 單筆投入的優勢",
                "✓ 資金效率高\n✓ 長期報酬率通常較高\n✓ 適合有一筆閒置資金時",
                "## 實戰建議",
                "如果你有穩定收入，建議每月定期定額。如果有一筆年終獎金，可以考慮分批單筆投入。",
            ],
        },
        {
            "title": "台股技術指標入門：KD、MACD、RSI 一次看懂",
            "tags": ["技術分析", "台股", "指標"],
            "body": [
                "## 三大技術指標速覽",
                "技術指標是投資人判斷買賣時機的工具。本文介紹最常用的三種。",
                "## KD 隨機指標",
                "KD 值 > 80 為超買區（可能過熱），< 20 為超賣區（可能反彈）。",
                "## MACD 指數平滑異同移動平均線",
                "當快線（DIF）向上突破慢線（MACD）為黃金交叉，是買進訊號。",
                "## RSI 相對強弱指標",
                "RSI > 70 表示超買，< 30 表示超賣。",
                "## 小提醒",
                "技術指標只是輔助工具，建議搭配基本面分析和風險管理使用。",
            ],
        },
    ],
    "productivity": [
        {
            "title": "5個免費生產力工具提升你的工作效率200%",
            "tags": ["生產力", "工具", "效率"],
            "body": [
                "## 為什麼需要生產力工具？",
                "在資訊爆炸的時代，懂得用工具的人比只會埋頭苦幹的人更有效率。",
                "## 1. Notion — 一站式知識管理",
                "筆記、資料庫、專案管理全部在一個工具完成。免費版就很夠用。",
                "## 2. Obsidian — 雙向連結筆記",
                "以「筆記連結」的方式組織知識，非常適合長期學習和研究。",
                "## 3. Todoist — 任務管理",
                "跨平台待辦事項管理，支援自然語言輸入。",
                "## 4. Forest — 專注計時",
                "結合番茄工作法和遊戲化，種虛擬樹讓你放下手機。",
                "## 5. GitHub — 不只是程式碼",
                "免費靜態網站託管（GitHub Pages），可以建立個人部落格和作品集。",
            ],
        },
        {
            "title": "番茄工作法實戰：如何每天專注8小時",
            "tags": ["生產力", "時間管理", "番茄鐘"],
            "body": [
                "## 什麼是番茄工作法？",
                "每工作25分鐘休息5分鐘，每4個番茄鐘休息15-30分鐘。",
                "## 為什麼有效？",
                "1. 短時間衝刺降低拖延心理負擔\n2. 強制休息避免過度疲勞\n3. 可量化的工作單位提升成就感",
                "## 實戰技巧",
                "• 每次只做一件事\n• 番茄鐘不可中斷\n• 記錄每天完成了幾個番茄鐘\n• 逐步調整為適合你的節奏",
            ],
        },
    ],
    "tech": [
        {
            "title": "GitHub Actions 自動化教學：從入門到實戰",
            "tags": ["GitHub Actions", "自動化", "DevOps"],
            "body": [
                "## 什麼是 GitHub Actions？",
                "GitHub Actions 是 GitHub 提供的 CI/CD 服務，可以自動化軟體開發工作流程。",
                "## 基本概念",
                "• Workflow: 自動化流程定義\n• Job: 一組步驟的集合\n• Step: 單一操作\n• Action: 可重複使用的步驟模組",
                "## 實用範例",
                "### 1. 自動部署 GitHub Pages",
                "當你 push 到 main 分支時自動建立靜態網站。",
                "### 2. 每日排程任務",
                "使用 cron 語法設定每日定時執行，適合爬蟲、內容生成等。",
                "### 3. 自動測試",
                "每次 PR 自動跑測試，確保程式碼品質。",
            ],
        },
        {
            "title": "免費域名 × GitHub Pages：建立你的個人品牌",
            "tags": ["GitHub Pages", "個人品牌", "免費資源"],
            "body": [
                "## 為什麼要用 GitHub Pages？",
                "完全免費、支援自訂域名、可綁定 Google Analytics。",
                "## 設定步驟",
                "1. 建立 repo: username.github.io\n2. push index.html\n3. 設定自訂域名（可從 Freenom 取得免費域名）\n4. 設定 DNS CNAME 記錄",
                "## 可做的網站類型",
                "• 個人部落格\n• 作品集\n• 工具站（計算機、轉換器）\n• 公司形象頁",
            ],
        },
    ],
}


def generate_post(template: dict) -> str:
    """Generate a markdown post from a template."""
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    slug = template["title"].lower().replace(" ", "-").replace("：", "-").replace("？", "")
    slug = "".join(c for c in slug if c.isalnum() or c in "-_")
    
    # Format tags
    tags_str = " ".join(f"[{t}]" for t in template["tags"])
    
    lines = [
        "---",
        f"layout: post",
        f"title: \"{template['title']}\"",
        f"date: {date_str}",
        f"tags: {tags_str}",
        f"description: \"{template['body'][1] if len(template['body']) > 1 else ''}\"",
        "---",
        "",
    ]
    lines.extend(template["body"])
    
    return "\n".join(lines)


def generate_posts(count: int = 3) -> list[str]:
    """Generate a set of SEO-optimized posts."""
    posts = []
    for category, templates in CONTENT_TEMPLATES.items():
        selected = random.sample(templates, min(1, len(templates)))
        for t in selected:
            posts.append(generate_post(t))
    return posts


def build_jekyll_site(posts: list[str]):
    """Build the GitHub Pages Jekyll site structure."""
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Write each post
    for i, post in enumerate(posts):
        # Extract title for filename
        title_line = [l for l in post.split("\n") if l.startswith("title:")]
        title = title_line[0].replace("title: ", "").strip('"') if title_line else f"post-{i}"
        slug = title.lower().replace(" ", "-").replace("：", "-")
        slug = "".join(c for c in slug if c.isalnum() or c in "-_")[:50]
        
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}.md"
        (POSTS_DIR / filename).write_text(post, encoding="utf-8")
        print(f"  ✅ {filename}")
    
    # Write index.html
    docs_dir = BASE_DIR / "docs"
    docs_dir.mkdir(exist_ok=True)
    
    post_links = ""
    for f in sorted(POSTS_DIR.glob("*.md"), reverse=True):
        title = f.read_text().split("\n")[2].replace("title: ", "").strip('"')
        post_links += f'<li><a href="/seo-blog{str(f).replace(str(POSTS_DIR), "").replace(".md", ".html")}">{title}</a></li>\n'
    
    index_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>知識部落格 — 投資/生產力/科技</title>
<meta name="description" content="免費台股投資教學、生產力工具心得、科技教學">
<style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family:-apple-system,sans-serif; background:#0f172a; color:#e2e8f0; max-width:800px; margin:auto; padding:20px; }}
    h1 {{ text-align:center; margin:20px 0; font-size:2rem; }}
    .post-list {{ list-style:none; }}
    .post-list li {{ background:#1e293b; margin:10px 0; padding:15px 20px; border-radius:12px; }}
    .post-list a {{ color:#3b82f6; text-decoration:none; font-size:1.1rem; }}
    .post-list a:hover {{ color:#60a5fa; }}
    .ad-placeholder {{ background:#1e293b; border:2px dashed #334155; border-radius:12px; padding:30px; text-align:center; margin:20px 0; color:#475569; }}
    footer {{ text-align:center; color:#475569; padding:20px; }}
</style>
<!-- Google AdSense (insert after approval) -->
</head>
<body>
    <h1>📝 知識部落格</h1>
    <p style="text-align:center;color:#64748b;">台股投資 · 生產力工具 · 科技教學</p>
    <div class="ad-placeholder">📢 AdSense 廣告區塊</div>
    <h2>最新文章</h2>
    <ul class="post-list">{post_links}</ul>
    <div class="ad-placeholder">📢 AdSense 廣告區塊</div>
    <footer>hermes-seo-farm · 每日自動更新 · <a href="https://github.com/slashman413/hermes-seo-farm" style="color:#3b82f6;">GitHub</a></footer>
</body>
</html>"""
    (docs_dir / "index.html").write_text(index_html, encoding="utf-8")
    print(f"✅ Generated index.html with {len(posts)} posts")


def main():
    print(f"📝 Generating SEO content for {datetime.now().strftime('%Y-%m-%d')}")
    posts = generate_posts(count=3)
    build_jekyll_site(posts)
    print(f"✅ Done: {len(posts)} posts created")


if __name__ == "__main__":
    main()
