#!/usr/bin/env python3
"""
hermes-seo-farm: Auto-generate SEO-optimized English HTML content for GitHub Pages.
Each run generates 3–5 articles across different niches as static .html files.
"""
import os, sys, json, random
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / "_posts"
DATA_DIR = BASE_DIR / "data"

CONTENT_TEMPLATES = {
    "investing": [
        {
            "title": "ETF vs Individual Stocks: Which Is Better for Beginners?",
            "tags": ["ETF", "Investing", "Beginner"],
            "body": [
                "## Why Compare ETFs and Individual Stocks?",
                "For new investors, the most common question is: should I buy ETFs or individual stocks?",
                "## 1. Risk Diversification",
                "ETFs track a basket of stocks, so one company's failure won't wipe you out. Individual stocks put all your eggs in one basket.",
                "## 2. Cost Comparison",
                "ETF expense ratios are typically under 0.5%. Individual stock investing requires time to research financials and technicals.",
                "## 3. Return Potential",
                "Individual stocks can deliver outsized returns (TSMC up 10x in a decade). ETFs deliver market-average returns.",
                "## Bottom Line",
                "For most investors, ETFs are a better starting point. Once you have experience, consider adding individual stocks.",
            ],
        },
        {
            "title": "Dollar-Cost Averaging vs Lump Sum: Which Strategy Wins?",
            "tags": ["DCA", "Investment Strategy", "Taiwan Stocks"],
            "body": [
                "## Two Investment Approaches",
                "Dollar-cost averaging (DCA) and lump sum investing each have pros and cons depending on your situation.",
                "## DCA Advantages",
                "✓ Spreads out purchase price risk\n✓ Perfect for monthly salary earners\n✓ Lower psychological stress",
                "## Lump Sum Advantages",
                "✓ Better capital efficiency\n✓ Higher long-term returns on average\n✓ Best when you have a cash windfall",
                "## Practical Advice",
                "If you have steady income, use DCA monthly. If you have a bonus or inheritance, consider phased lump sum investing.",
            ],
        },
        {
            "title": "Taiwan Stock Technical Analysis: KD, MACD, RSI Explained",
            "tags": ["Technical Analysis", "Taiwan Stocks", "Indicators"],
            "body": [
                "## Three Essential Indicators",
                "Technical indicators help investors time their entries and exits. Here are the three most popular ones.",
                "## KD Stochastic Oscillator",
                "KD > 80 indicates overbought (might be overheated). KD < 20 indicates oversold (might bounce back).",
                "## MACD (Moving Average Convergence Divergence)",
                "When the fast line (DIF) crosses above the slow line (MACD), it's a golden cross — a buy signal.",
                "## RSI (Relative Strength Index)",
                "RSI > 70 means overbought. RSI < 30 means oversold.",
                "## Reminder",
                "Technical indicators are tools, not guarantees. Always combine with fundamental analysis and risk management.",
            ],
        },
    ],
    "productivity": [
        {
            "title": "5 Free Productivity Tools That Will 2x Your Output",
            "tags": ["Productivity", "Tools", "Efficiency"],
            "body": [
                "## Why You Need Productivity Tools",
                "In the age of information overload, smart tool users consistently outperform those who grind manually.",
                "## 1. Notion — All-in-One Workspace",
                "Notes, databases, project management — all in one tool. The free plan is generous enough for most users.",
                "## 2. Obsidian — Bidirectional Linking",
                "Organize knowledge through linked notes. Perfect for long-term learning and research.",
                "## 3. Todoist — Task Management",
                "Cross-platform task management with natural language input.",
                "## 4. Forest — Focus Timer",
                "Pomodoro + gamification: grow virtual trees by staying off your phone.",
                "## 5. GitHub — More Than Code",
                "Free static site hosting (GitHub Pages). Build your blog and portfolio for free.",
            ],
        },
        {
            "title": "Pomodoro Technique: How to Focus for 8 Hours Daily",
            "tags": ["Productivity", "Time Management", "Pomodoro"],
            "body": [
                "## What Is the Pomodoro Technique?",
                "Work for 25 minutes, rest for 5. Take a 15-30 minute break every 4 pomodoros.",
                "## Why It Works",
                "1. Short sprints lower psychological resistance to starting\n2. Forced breaks prevent burnout\n3. Quantifiable work units boost satisfaction",
                "## Pro Tips",
                "• One task per pomodoro\n• Never interrupt a pomodoro\n• Track your daily pomodoro count\n• Adjust intervals to your rhythm",
            ],
        },
        {
            "title": "Build a Second Brain with Digital Notes",
            "tags": ["Second Brain", "Notes", "Knowledge Management"],
            "body": [
                "## What Is a Second Brain?",
                "A system for capturing, organizing, and retrieving ideas so you never lose a good thought again.",
                "## The PARA Method",
                "Organize everything into 4 folders:\n• Projects: Active outcomes\n• Areas: Ongoing responsibilities\n• Resources: Topics of interest\n• Archives: Inactive items",
                "## Tools to Use",
                "• Capture: Apple Notes / Google Keep\n• Organize: Notion / Obsidian\n• Retrieve: Built-in search + tags\n• Archive: Regular cleanup",
                "## Start Today",
                "Even 5 minutes of note-taking daily compounds into a powerful knowledge base over months.",
            ],
        },
    ],
    "tech": [
        {
            "title": "GitHub Actions Automation: From Zero to Production",
            "tags": ["GitHub Actions", "Automation", "DevOps"],
            "body": [
                "## What Is GitHub Actions?",
                "GitHub's built-in CI/CD service for automating software workflows — completely free for public repos.",
                "## Core Concepts",
                "• Workflow: Automated process definition\n• Job: Collection of steps\n• Step: Single operation\n• Action: Reusable module",
                "## Practical Examples",
                "### 1. Auto-Deploy GitHub Pages",
                "Build your static site automatically on every push to main.",
                "### 2. Scheduled Tasks",
                "Use cron syntax for daily data scraping, content generation, or report delivery.",
                "### 3. Auto-Testing",
                "Run tests on every PR to maintain code quality.",
            ],
        },
        {
            "title": "Free Domain + GitHub Pages: Build Your Personal Brand",
            "tags": ["GitHub Pages", "Personal Brand", "Free Resources"],
            "body": [
                "## Why GitHub Pages?",
                "Completely free, supports custom domains, works with Google Analytics.",
                "## Setup Steps",
                "1. Create repo: username.github.io\n2. Push index.html\n3. Set custom domain\n4. Configure DNS CNAME record",
                "## What You Can Build",
                "• Personal blog\n• Portfolio\n• Tool site (calculators, converters)\n• Business landing page",
            ],
        },
        {
            "title": "Python Script to Automate Your Daily Tasks",
            "tags": ["Python", "Automation", "Scripting"],
            "body": [
                "## Why Automate with Python?",
                "Python is the easiest language to automate repetitive tasks. Plus it runs everywhere.",
                "## 5 Things You Can Automate Today",
                "### 1. File Organization",
                "Auto-sort your Downloads folder by file type.",
                "### 2. Email Reports",
                "Schedule daily email digests with Python + SMTP.",
                "### 3. Web Scraping",
                "Track prices, news, or data changes automatically.",
                "### 4. Social Media Posts",
                "Schedule tweets and posts with Python scripts.",
                "### 5. Data Backup",
                "Auto-backup important folders to cloud storage.",
            ],
        },
    ],
    "psychology": [
        {
            "title": "The Psychology of Habits: Why 1% Daily Improvement Matters",
            "tags": ["Psychology", "Habits", "Self-Improvement"],
            "body": [
                "## The Power of Small Wins",
                "Improving just 1% every day makes you 37x better after one year. The math is simple; the execution is hard.",
                "## Why Habits Stick (or Don't)",
                "The habit loop: Cue → Craving → Response → Reward. Most people fail because they focus on the outcome, not the system.",
                "## Atomic Habits in Practice",
                "• Make it obvious (cue)\n• Make it attractive (craving)\n• Make it easy (response)\n• Make it satisfying (reward)",
                "## Start Your 1% Today",
                "Pick one tiny habit. Do it for 2 minutes. Repeat tomorrow. That's all it takes.",
            ],
        },
        {
            "title": "Stoicism for Modern Life: Ancient Wisdom That Still Works",
            "tags": ["Stoicism", "Philosophy", "Mental Health"],
            "body": [
                "## What Is Stoicism?",
                "An ancient Greek philosophy focused on what you can control and accepting what you cannot.",
                "## The Dichotomy of Control",
                "Some things are up to you (thoughts, actions, opinions). Others are not (weather, others' opinions, the past). Focus only on the first.",
                "## Daily Stoic Practices",
                "• Morning: Prepare for challenges\n• Throughout the day: Pause before reacting\n• Evening: Review your actions",
                "## Modern Applications",
                "Stoicism helps with: anxiety reduction, better decision-making, emotional resilience, and focusing on what truly matters.",
            ],
        },
    ],
    "ai_tools": [
        {
            "title": "5 AI Tools That Actually Save You Time (Not Just Hype)",
            "tags": ["AI", "Tools", "Productivity"],
            "body": [
                "## The AI Tool Landscape in 2026",
                "With hundreds of AI tools launching weekly, here are 5 that have proven real value.",
                "## 1. Cursor — AI Code Editor",
                "VS Code + AI. Write code 10x faster with inline suggestions and chat.",
                "## 2. Claude — Reasoning Assistant",
                "Best for complex analysis, writing, and coding with long context windows.",
                "## 3. Perplexity — AI Search Engine",
                "Get answers with citations instead of link lists. Great for research.",
                "## 4. Notion AI — Writing Assistant",
                "Generate summaries, drafts, and translations inside your existing workspace.",
                "## 5. GitHub Copilot — Code Completion",
                "Autocomplete for any programming language. Learn by doing.",
            ],
        },
        {
            "title": "How to Use AI to Write SEO Content That Ranks",
            "tags": ["SEO", "AI Content", "Marketing"],
            "body": [
                "## Does AI Content Rank on Google?",
                "Yes — Google rewards quality, regardless of who (or what) writes it.",
                "## The Right Way to Use AI for SEO",
                "• Use AI for research and outlines\n• Add your unique experience and data\n• Fact-check everything\n• Optimize for humans first, search engines second",
                "## Structure That Works",
                "1. Hook in the first 100 words\n2. Clear H2/H3 subheadings\n3. Bullet points for scannability\n4. Internal/External links\n5. Strong conclusion with CTA",
                "## Tools for SEO Content",
                "• Generate outlines: Claude\n• Write drafts: ChatGPT/Claude\n• Optimize: Surfer SEO\n• Analyze: Google Search Console",
            ],
        },
    ],
}


def md_to_html(text: str) -> str:
    """Convert simple markdown to HTML for inline rendering."""
    lines = text.split("\n")
    html_parts = []
    in_list = False
    list_type = None  # 'ul' or 'ol'
    in_nested_section = False
    for line in lines:
        stripped = line.strip()
        # Empty line
        if not stripped:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
                list_type = None
            html_parts.append("<br>")
            continue
        # Headings
        if stripped.startswith("### "):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False; list_type = None
            html_parts.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith("## "):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False; list_type = None
            html_parts.append(f"<h2>{stripped[3:]}</h2>")
        # Bullet list
        elif stripped.startswith("• ") or stripped.startswith("- ") or stripped.startswith("* "):
            txt = stripped.lstrip("•-* ")
            if not in_list or list_type != "ul":
                if in_list: html_parts.append(f"</{list_type}>")
                html_parts.append("<ul>")
                in_list = True; list_type = "ul"
            html_parts.append(f"<li>{txt}</li>")
        # Numbered list
        elif len(stripped) > 2 and stripped[0].isdigit() and stripped[1:3] in (". ", ") "):
            txt = stripped.split(". ", 1)[1] if ". " in stripped else stripped.split(") ", 1)[1]
            if not in_list or list_type != "ol":
                if in_list: html_parts.append(f"</{list_type}>")
                html_parts.append("<ol>")
                in_list = True; list_type = "ol"
            html_parts.append(f"<li>{txt}</li>")
        else:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False; list_type = None
            html_parts.append(f"<p>{stripped}</p>")
    if in_list:
        html_parts.append(f"</{list_type}>")
    return "\n".join(html_parts)


def generate_post_html(template: dict, date_str: str) -> tuple[str, str]:
    """Generate a full HTML post and return (html_content, slug)."""
    slug = template["title"].lower().replace(" ", "-").replace(":", "").replace("?", "")
    slug = "".join(c for c in slug if c.isalnum() or c in "-_")[:60]

    tags_html = " ".join(f'<span class="tag">{t}</span>' for t in template["tags"])
    body_html = md_to_html("\n".join(template["body"]))
    description = template["body"][1] if len(template["body"]) > 1 else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{template['title']}</title>
<meta name="description" content="{description}">
<style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; background:#0f172a; color:#e2e8f0; max-width:720px; margin:auto; padding:20px; line-height:1.8; font-size:16px; }}
    h1 {{ margin:30px 0 10px; font-size:1.8rem; line-height:1.3; }}
    h2 {{ color:#60a5fa; margin:25px 0 10px; font-size:1.3rem; border-bottom:1px solid #1e293b; padding-bottom:5px; }}
    h3 {{ color:#93c5fd; margin:20px 0 8px; font-size:1.1rem; }}
    p {{ margin:12px 0; }}
    ul, ol {{ margin:10px 0 10px 24px; }}
    li {{ margin:5px 0; }}
    .tags {{ margin:10px 0 20px; }}
    .tag {{ display:inline-block; background:#1e293b; color:#38bdf8; padding:2px 10px; border-radius:12px; font-size:0.8rem; margin-right:5px; }}
    .date {{ color:#64748b; font-size:0.85rem; margin-bottom:20px; }}
    .ad {{ background:#1e293b; border:2px dashed #334155; border-radius:12px; padding:30px; text-align:center; margin:30px 0; color:#475569; }}
    a {{ color:#3b82f6; }}
    a:hover {{ color:#60a5fa; }}
    .back {{ display:inline-block; margin:20px 0; color:#64748b; text-decoration:none; font-size:0.9rem; }}
    .back:hover {{ color:#3b82f6; }}
    footer {{ text-align:center; color:#475569; padding:30px 0; font-size:0.85rem; }}
</style>
</head>
<body>
    <a href="../index.html" class="back">&larr; Back to Blog</a>
    <h1>{template['title']}</h1>
    <div class="date">{date_str}</div>
    <div class="tags">{tags_html}</div>
    <div class="ad">📢 AdSense Ad Unit (enable after approval)</div>
{body_html}
    <div class="ad">📢 AdSense Ad Unit (enable after approval)</div>
    <footer>
        <p>Auto-generated daily by hermes-seo-farm</p>
        <p><a href="https://github.com/slashman413/hermes-seo-farm">GitHub</a></p>
    </footer>
</body>
</html>"""
    return html, slug


def generate_posts(count: int = 5) -> list[tuple[str, str, str]]:
    """Generate a set of SEO-optimized posts across categories.
    Returns list of (html_content, slug, title).
    """
    posts = []
    categories = list(CONTENT_TEMPLATES.keys())
    random.shuffle(categories)
    today = datetime.now().strftime("%Y-%m-%d")

    # Pick at least 1 from each category, up to count
    for category in categories:
        templates = CONTENT_TEMPLATES[category]
        selected = random.sample(templates, min(1, len(templates)))
        for t in selected:
            if len(posts) < count:
                html_content, slug = generate_post_html(t, today)
                posts.append((html_content, slug, t["title"]))

    return posts


def build_site(posts: list[tuple[str, str, str]]):
    """Build the GitHub Pages site as static HTML files."""
    docs_dir = BASE_DIR / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    posts_dir = docs_dir / "_posts"
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Write each post as .html
    for html, slug, title in posts:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}.html"
        (posts_dir / filename).write_text(html, encoding="utf-8")
        print(f"  ✅ {filename}")

    # Build index.html
    post_links = ""
    for f in sorted(posts_dir.glob("*.html"), reverse=True):
        # Extract title from HTML
        content = f.read_text(encoding="utf-8")
        title_start = content.find("<title>")
        title_end = content.find("</title>")
        t = content[title_start + 7:title_end] if title_start >= 0 else f.name
        post_links += f'<li><a href="_posts/{f.name}">{t}</a> <span class="date">{f.name[:10]}</span></li>\n'

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog — Investing, Productivity, Tech & AI</title>
<meta name="description" content="Free articles on Taiwan stock investing, productivity tools, tech tutorials, psychology, and AI.">
<style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; background:#0f172a; color:#e2e8f0; max-width:800px; margin:auto; padding:20px; }}
    h1 {{ text-align:center; margin:20px 0; font-size:2rem; }}
    .subtitle {{ text-align:center; color:#64748b; margin-bottom:20px; }}
    .post-list {{ list-style:none; padding:0; }}
    .post-list li {{ background:#1e293b; margin:10px 0; padding:15px 20px; border-radius:12px; display:flex; justify-content:space-between; align-items:center; }}
    .post-list a {{ color:#3b82f6; text-decoration:none; font-size:1.1rem; }}
    .post-list a:hover {{ color:#60a5fa; }}
    .post-list .date {{ color:#64748b; font-size:0.85rem; white-space:nowrap; }}
    .ad {{ background:#1e293b; border:2px dashed #334155; border-radius:12px; padding:30px; text-align:center; margin:20px 0; color:#475569; }}
    footer {{ text-align:center; color:#475569; padding:20px; }}
</style>
</head>
<body>
    <h1>📝 Knowledge Blog</h1>
    <p class="subtitle">Taiwan Stocks · Productivity · Tech · Psychology · AI</p>
    <div class="ad">📢 AdSense Ad Unit (enable after approval)</div>
    <h2>Latest Articles</h2>
    <ul class="post-list">{post_links}</ul>
    <div class="ad">📢 AdSense Ad Unit (enable after approval)</div>
    <footer>
        <p>Auto-generated daily by hermes-seo-farm</p>
        <p><a href="https://github.com/slashman413/hermes-seo-farm" style="color:#3b82f6;">GitHub</a></p>
    </footer>
</body>
</html>"""
    (docs_dir / "index.html").write_text(index_html, encoding="utf-8")
    print(f"✅ Generated index.html with {len(posts)} posts")


def main():
    print(f"📝 Generating SEO content for {datetime.now().strftime('%Y-%m-%d')}")
    posts = generate_posts(count=5)
    build_site(posts)
    print(f"✅ Done: {len(posts)} HTML posts created")


if __name__ == "__main__":
    main()
