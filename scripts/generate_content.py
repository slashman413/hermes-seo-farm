#!/usr/bin/env python3
"""
hermes-seo-farm: Auto-generate SEO-optimized English HTML content for GitHub Pages.
Each run generates 3–5 articles with product recommendations and AdSense support.
"""
import os, sys, json, random
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / "docs" / "_posts"
DATA_DIR = BASE_DIR / "data"

# Product recommendations by category
PRODUCT_CTAS = {
    "investing": {
        "name": "TWSE Premium",
        "url": "https://ko-fi.com/s/b99720d13d",
        "text": "📊 Want real-time Taiwan stock signals? TWSE Premium scans 1800+ stocks daily and emails you buy/sell alerts. Try it now →",
        "price": "$49/mo",
    },
    "productivity": {
        "name": "Free Online Tools",
        "url": "https://slashmantools.us/",
        "text": "🔧 Boost your productivity with 20+ free online tools — calculators, PDF tools, QR generator, and more. No sign-up needed →",
        "price": "Free",
    },
    "tech": {
        "name": "GitHub Tools Collection",
        "url": "https://github.com/slashman413",
        "text": "💻 Explore 20+ open-source projects on GitHub — all free, all automated with GitHub Actions →",
        "price": "Free & Open Source",
    },
    "psychology": {
        "name": "Gentle Soul YouTube",
        "url": "https://www.youtube.com/@GentleSoul666",
        "text": "💭 Need daily inspiration? Subscribe to Gentle Soul for daily quote shorts with piano music →",
        "price": "Free",
    },
    "ai_tools": {
        "name": "SEO Content Engine",
        "url": "https://ko-fi.com/s/a03f0a8e3b",
        "text": "🤖 Generate SEO content automatically like this article! SEO Content Engine creates optimized articles daily on GitHub Pages →",
        "price": "$19/mo",
    },
    "deals": {
        "name": "Deal Finder Pro",
        "url": "https://ko-fi.com/s/5730f8f947",
        "text": "🛒 Never miss an Amazon deal again! Deal Finder Pro automatically tracks and notifies you of the best discounts →",
        "price": "$19/mo",
    },
}

ALL_CATEGORIES = list(PRODUCT_CTAS.keys())

CONTENT_TEMPLATES = {
    "investing": [
        {
            "title": "ETF vs Individual Stocks: Which Is Better for Beginners?",
            "category": "investing",
            "tags": ["ETF", "Investing", "Beginner", "Taiwan Stocks"],
            "body": [
                "## Why Compare ETFs and Individual Stocks?",
                "For new investors, the most common question is: should I buy ETFs or individual stocks? Both have passionate advocates, and the right answer depends on your goals, time commitment, and risk tolerance.",
                "## 1. Risk Diversification",
                "ETFs track a basket of stocks, so one company's failure won't wipe you out. Individual stocks put all your eggs in one basket. With a TWSE ETF like 0050, you own Taiwan's top 50 companies in one trade.",
                "## 2. Cost Comparison",
                "ETF expense ratios are typically under 0.5%. Individual stock investing requires time to research financials and technicals. For beginners, ETFs offer a much lower time investment.",
                "## 3. Return Potential",
                "Individual stocks can deliver outsized returns (TSMC up 10x in a decade). ETFs deliver market-average returns. Most professional fund managers fail to beat the market consistently.",
                "## Bottom Line",
                "For most investors, ETFs are a better starting point. Once you have experience, consider adding individual stocks. Use tools like TWSE Premium to get real-time signals on both.",
            ],
        },
        {
            "title": "Dollar-Cost Averaging vs Lump Sum: Which Strategy Wins?",
            "category": "investing",
            "tags": ["DCA", "Investment Strategy", "Taiwan Stocks"],
            "body": [
                "## Two Investment Approaches",
                "Dollar-cost averaging (DCA) and lump sum investing each have pros and cons depending on your situation. Understanding when to use each can significantly impact your long-term returns.",
                "## DCA Advantages",
                "• Spreads out purchase price risk<br>• Perfect for monthly salary earners<br>• Lower psychological stress<br>• Works well in volatile markets",
                "## Lump Sum Advantages",
                "• Better capital efficiency in bull markets<br>• Higher long-term returns on average<br>• Best when you have a cash windfall<br>• Simpler to execute (one trade)",
                "## Practical Advice",
                "If you have steady income, use DCA monthly through automatic investments. If you receive a large bonus or inheritance, consider a phased approach: invest 50% immediately, then DCA the rest over 6 months.",
            ],
        },
        {
            "title": "Taiwan Stock Technical Analysis: KD, MACD, RSI Explained",
            "category": "investing",
            "tags": ["Technical Analysis", "Taiwan Stocks", "Indicators", "TWSE"],
            "body": [
                "## Three Essential Indicators",
                "Technical indicators help investors time their entries and exits. Here are the three most popular ones used by Taiwan stock traders.",
                "## KD Stochastic Oscillator",
                "KD > 80 indicates overbought (might be overheated). KD < 20 indicates oversold (might bounce back). The K line crossing above the D line is a common entry signal.",
                "## MACD (Moving Average Convergence Divergence)",
                "When the fast line (DIF) crosses above the slow line (MACD), it's a golden cross — a buy signal. When DIF crosses below, it's a death cross — a sell signal.",
                "## RSI (Relative Strength Index)",
                "RSI > 70 means overbought. RSI < 30 means oversold. Divergence between price and RSI is one of the most reliable reversal signals.",
                "## Let Automation Do the Work",
                "Instead of manually checking indicators for 1800+ stocks daily, use automated scanners like TWSE Premium that calculate all three indicators and email you the signals instantly.",
            ],
        },
        {
            "title": "0050 vs 0056: Which Taiwan ETF Should You Buy?",
            "category": "investing",
            "tags": ["ETF", "0050", "0056", "Taiwan"],
            "body": [
                "## Taiwan's Two Most Popular ETFs",
                "0050 (Yuanta Taiwan 50) tracks the top 50 companies by market cap. 0056 (Yuanta Taiwan High Dividend) tracks 50 high-dividend stocks. Which one is right for you?",
                "## 0050 — Growth Focus",
                "• Heavy TSMC weighting (~48%)<br>• Tracks the overall market<br>• Higher growth potential<br>• Lower dividend yield (~3%)<br>• Best for young investors with long time horizons",
                "## 0056 — Income Focus",
                "• Selects stocks with highest dividends<br>• Lower TSMC exposure<br>• Higher dividend yield (~5-6%)<br>• More stable during downturns<br>• Best for retirees or income seekers",
                "## The Smart Approach",
                "Many Taiwan investors hold both: 70% in 0050 for growth and 30% in 0056 for dividends. Rebalance annually. Use free portfolio tracking tools to monitor your allocation.",
            ],
        },
        {
            "title": "Stop Loss Strategies: How to Protect Your Portfolio",
            "category": "investing",
            "tags": ["Risk Management", "Stop Loss", "Trading"],
            "body": [
                "## Why Every Trader Needs a Stop Loss",
                "The difference between successful and unsuccessful traders often comes down to risk management. A stop loss is your most important protection tool.",
                "## Fixed Percentage Stop Loss",
                "Set a fixed percentage below your entry price. Common settings: 5% for volatile stocks, 3% for stable stocks. This removes emotion from your selling decisions.",
                "## Trailing Stop Loss",
                "As the stock price rises, your stop loss moves up with it. This locks in profits while giving the stock room to grow. Most platforms support this automatically.",
                "## Technical Stop Loss",
                "Place your stop below key support levels: recent lows, moving averages, or trendlines. This aligns your exit with technical analysis rather than arbitrary percentages.",
                "## Automate Your Risk Management",
                "Manual stop loss tracking for a portfolio of stocks is time-consuming. Automated scanning tools can monitor all your positions and alert you when any hit your stop loss levels.",
            ],
        },
        {
            "title": "Dividend Investing in Taiwan: A Complete Guide",
            "category": "investing",
            "tags": ["Dividend", "Passive Income", "Taiwan Stocks"],
            "body": [
                "## Why Dividend Investing Works in Taiwan",
                "Taiwan stocks have historically paid among the highest dividend yields in Asia. Combined with Taiwan's favorable tax treatment for dividends, it's an attractive market for income investors.",
                "## Top Dividend Stocks to Watch",
                "• TSMC (2330): Growing dividend, not high yield<br>• Chunghwa Telecom (2412): Stable ~4% yield<br>• Formosa Plastics (1301): Cyclical but high yield<br>• Cathay Financial (2882): Financial sector dividends",
                "## Reinvestment Strategy (DRIP)",
                "The real power of dividend investing comes from reinvestment. Over 20 years, reinvested dividends can account for 40-50% of total returns. Most Taiwan brokerages offer automatic DRIP.",
                "## Screening for Dividends",
                "Instead of manually checking dividend histories for 1800+ stocks, use screening tools that filter by dividend yield, payout ratio, and consecutive years of payments.",
            ],
        },
    ],
    "productivity": [
        {
            "title": "5 Free Productivity Tools That Will 2x Your Output",
            "category": "productivity",
            "tags": ["Productivity", "Tools", "Efficiency"],
            "body": [
                "## Why You Need Productivity Tools",
                "In the age of information overload, smart tool users consistently outperform those who grind manually. The best tools are free and require no setup.",
                "## 1. Free Online Calculators",
                "Need a quick BMI, percentage, or loan calculator? Use free web-based tools that work instantly in your browser — no downloads, no sign-ups.",
                "## 2. PDF Tools Online",
                "Convert images to PDF, merge multiple PDFs, or compress files — all from your browser. Perfect for students and office workers.",
                "## 3. QR Code Generator",
                "Generate QR codes for URLs, text, or WiFi passwords in seconds. Free, no account needed, high-resolution output.",
                "## 4. Image Compressor",
                "Reduce image file sizes without losing quality. Essential for web developers and anyone who sends images via email.",
                "## 5. Color Tools & Palettes",
                "Pick colors, generate gradients, and test contrast ratios. Free tools for designers and developers.",
            ],
        },
        {
            "title": "Pomodoro Technique: How to Focus for 8 Hours Daily",
            "category": "productivity",
            "tags": ["Productivity", "Time Management", "Pomodoro"],
            "body": [
                "## What Is the Pomodoro Technique?",
                "Work for 25 minutes, rest for 5. Take a 15-30 minute break every 4 pomodoros. Simple, effective, and backed by decades of user experience.",
                "## Why It Works",
                "1. Short sprints lower psychological resistance to starting tasks<br>2. Forced breaks prevent burnout and maintain quality<br>3. Quantifiable work units (pomodoros) boost satisfaction<br>4. The timer creates urgency without anxiety",
                "## Pro Tips for Maximum Focus",
                "• One task per pomodoro — no multitasking<br>• Never interrupt a pomodoro mid-way<br>• Track your daily pomodoro count<br>• Adjust intervals to your natural rhythm (try 52/17 for deep work)<br>• Use a physical timer for the analog effect",
                "## Free Focus Timer",
                "Try a free online Pomodoro timer with built-in white noise. No installation needed — works in any browser with zero setup.",
            ],
        },
        {
            "title": "Build a Second Brain with Digital Notes",
            "category": "productivity",
            "tags": ["Second Brain", "Notes", "Knowledge Management"],
            "body": [
                "## What Is a Second Brain?",
                "A system for capturing, organizing, and retrieving ideas so you never lose a good thought again. Popularized by Tiago Forte's book.",
                "## The PARA Method",
                "Organize everything into 4 folders:<br>• Projects: Active outcomes with deadlines<br>• Areas: Ongoing responsibilities (health, finances)<br>• Resources: Topics of interest<br>• Archives: Inactive items from the other three",
                "## Free Tools to Start Today",
                "• Capture: Use simple text tools or note apps<br>• Organize: Folder-based systems work fine<br>• Retrieve: Use search + consistent tagging<br>• Archive: Weekly cleanup habit",
                "## Start Your Second Brain",
                "Even 5 minutes of daily note-taking compounds into a powerful knowledge base over months. The key is consistency, not complexity.",
            ],
        },
        {
            "title": "How to Build a Daily Routine That Actually Sticks",
            "category": "productivity",
            "tags": ["Habits", "Routine", "Self-Improvement"],
            "body": [
                "## Why Most Routines Fail",
                "Most people fail at routines because they try to change too much at once. The secret is to start so small that it's impossible to say no.",
                "## The 2-Minute Rule",
                "Scale down any habit to 2 minutes:",
                "• 'Read more' → 'Read one page'<br>• 'Exercise more' → 'Put on workout clothes'<br>• 'Write daily' → 'Write one sentence'<br>• 'Meditate' → 'Breathe three times'",
                "## Stack Your Habits",
                "After [existing habit], I will [new habit]. Examples:<br>• After my morning coffee, I will write for 2 minutes<br>• After brushing teeth, I will do 5 squats<br>• After lunch, I will walk for 5 minutes",
                "## Track with Free Tools",
                "Use a free online habit tracker, Pomodoro timer, or simple checklist. The act of checking off a completed habit releases dopamine and reinforces the behavior.",
            ],
        },
    ],
    "tech": [
        {
            "title": "GitHub Actions Automation: From Zero to Production",
            "category": "tech",
            "tags": ["GitHub Actions", "Automation", "DevOps"],
            "body": [
                "## What Is GitHub Actions?",
                "GitHub's built-in CI/CD service for automating software workflows — completely free for public repos. It runs on Ubuntu, Windows, and macOS runners.",
                "## Core Concepts",
                "• Workflow: A YAML file defining your automated process<br>• Job: A collection of steps running on the same runner<br>• Step: A single operation (run a command or use an action)<br>• Action: A reusable custom module from the marketplace",
                "## Practical Examples You Can Build Today",
                "### 1. Auto-Deploy GitHub Pages",
                "On every push to main, automatically build and deploy your static site. Perfect for blogs and documentation.",
                "### 2. Scheduled Content Generation",
                "Use cron syntax to run daily tasks: data scraping, report generation, or social media posting — all for free.",
                "### 3. Automated Testing",
                "Run tests on every pull request and block merges if tests fail. Essential for maintaining code quality in teams.",
                "## Real-World Example",
                "This very blog is auto-generated by a scheduled GitHub Actions workflow! Each day, new articles are created, formatted, and deployed to GitHub Pages automatically.",
            ],
        },
        {
            "title": "Free Domain + GitHub Pages: Build Your Personal Brand",
            "category": "tech",
            "tags": ["GitHub Pages", "Personal Brand", "Free Resources"],
            "body": [
                "## Why GitHub Pages?",
                "Completely free hosting for static sites, supports custom domains, works with Google Analytics, and has built-in SSL certificates.",
                "## Setup Steps",
                "1. Create a repository named username.github.io<br>2. Push your HTML/CSS/JS files<br>3. (Optional) Set a custom domain in repo settings<br>4. Configure your DNS provider with a CNAME record<br>5. Your site is live at your custom domain within minutes",
                "## What You Can Build for Free",
                "• Personal blog with daily articles<br>• Portfolio showcasing your work<br>• Tool site with calculators and converters<br>• Business landing page with contact form<br>• Documentation site for an open-source project",
                "## Monetization Options",
                "Add Google AdSense, affiliate links, or product listings to generate passive income from your free GitHub Pages site.",
            ],
        },
        {
            "title": "Python Script to Automate Your Daily Tasks",
            "category": "tech",
            "tags": ["Python", "Automation", "Scripting"],
            "body": [
                "## Why Automate with Python?",
                "Python is the easiest language to automate repetitive tasks. It runs everywhere and has libraries for everything. Best of all, you can run Python scripts for free on GitHub Actions.",
                "## 5 Things You Can Automate Today",
                "### 1. File Organization",
                "Auto-sort your Downloads folder by file type. Images go to Pictures, PDFs go to Documents, etc. A 10-line script can save you hours monthly.",
                "### 2. Email Reports",
                "Schedule daily email digests with Python + SMTP. Perfect for sending portfolio updates, weather reports, or news summaries.",
                "### 3. Web Scraping",
                "Track prices, monitor news, or collect data automatically. Use BeautifulSoup or Selenium for dynamic content.",
                "### 4. Social Media Posts",
                "Schedule tweets and posts automatically. Post at optimal times even when you're asleep.",
                "### 5. Data Backup Automation",
                "Auto-backup important folders to cloud storage on a schedule. Never lose data again.",
            ],
        },
        {
            "title": "Free Tools Every Developer Should Know About",
            "category": "tech",
            "tags": ["Developer Tools", "Free Resources", "Productivity"],
            "body": [
                "## Build Faster with Free Tools",
                "Professional developers rely on tools to speed up their workflow. Here are essential free tools every developer should bookmark.",
                "## Online Developer Tools",
                "• Base64 encoder/decoder — for handling encoded data<br>• URL encoder/decoder — for API testing<br>• JSON formatter — for debugging API responses<br>• JWT decoder — for authentication debugging<br>• Regex tester — for pattern matching",
                "## Design Tools",
                "• Color palette generator — create harmonious color schemes<br>• Gradient maker — design beautiful CSS gradients<br>• Contrast checker — ensure WCAG accessibility compliance<br>• Image compressor — optimize web images",
                "## Utility Tools",
                "• QR code generator — for quick mobile links<br>• Word counter — for content length checks<br>• Unit converter — for measurement conversions<br>• Password generator — for secure credentials",
                "All of these are available as free online tools — no installs, no sign-ups.",
            ],
        },
    ],
    "ai_tools": [
        {
            "title": "How to Use AI to Write SEO Content That Ranks",
            "category": "ai_tools",
            "tags": ["SEO", "AI Content", "Marketing"],
            "body": [
                "## Does AI Content Rank on Google?",
                "Yes — Google rewards quality content regardless of who (or what) writes it. The key is adding value, not just generating word count.",
                "## The Right Way to Use AI for SEO",
                "• Use AI for research and outlines first<br>• Add your unique experience and data<br>• Fact-check everything before publishing<br>• Optimize for humans first, search engines second<br>• Update content regularly to maintain freshness",
                "## Article Structure That Ranks",
                "1. Hook readers in the first 100 words<br>2. Clear H2/H3 subheadings (helps featured snippets)<br>3. Bullet points for scannability<br>4. Internal links to related content<br>5. External links to authoritative sources<br>6. Strong conclusion with call-to-action",
                "## Automate Your Content Pipeline",
                "Services like SEO Content Engine use AI to generate, format, and deploy SEO-optimized articles daily to GitHub Pages — exactly like this article you're reading now.",
            ],
        },
        {
            "title": "5 AI Tools That Actually Save You Time",
            "category": "ai_tools",
            "tags": ["AI", "Tools", "Productivity"],
            "body": [
                "## The AI Tool Landscape",
                "With hundreds of AI tools launching weekly, here are 5 that have proven real value for professionals.",
                "## 1. AI Code Assistants",
                "Write code faster with inline suggestions and context-aware completions. Great for both beginners and experienced developers.",
                "## 2. AI Writing Assistants",
                "Generate summaries, drafts, and translations inside your workflow. Best for content creators and marketers.",
                "## 3. AI Search Engines",
                "Get answers with citations instead of link lists. Transform how you do research.",
                "## 4. AI Image Generators",
                "Create custom images, thumbnails, and illustrations for your content. No design skills needed.",
                "## 5. AI Video Generators",
                "Automatically create short videos from text scripts. Perfect for social media content creators.",
            ],
        },
        {
            "title": "ChatGPT vs Claude vs Gemini: Which AI Is Best for You?",
            "category": "ai_tools",
            "tags": ["AI", "ChatGPT", "Comparison"],
            "body": [
                "## The Big Three AI Assistants",
                "ChatGPT (OpenAI), Claude (Anthropic), and Gemini (Google) lead the AI assistant market. Each has unique strengths depending on your use case.",
                "## ChatGPT — Best All-Rounder",
                "Strengths: Large plugin ecosystem, DALL-E image generation, voice mode, huge user community. Best for general tasks, brainstorming, and creative projects.",
                "## Claude — Best for Analysis",
                "Strengths: Longest context window (200K tokens), nuanced reasoning, strong safety guardrails. Best for document analysis, research, and complex problem-solving.",
                "## Gemini — Best for Google Integration",
                "Strengths: Native Google Workspace integration, real-time web data access, multimodal by default. Best for Google users and fact-checking.",
                "## The Pragmatic Choice",
                "Most power users subscribe to multiple services. Use the right tool for each task rather than relying on a single assistant.",
            ],
        },
        {
            "title": "Prompt Engineering: Write Better AI Prompts in 2026",
            "category": "ai_tools",
            "tags": ["Prompt Engineering", "AI", "Tips"],
            "body": [
                "## Why Prompt Engineering Matters",
                "The quality of AI output depends directly on the quality of your input. Learning to write effective prompts saves hours of editing.",
                "## The COSTAR Framework",
                "• Context: Give background information<br>• Objective: State your goal clearly<br>• Style: Specify tone and format<br>• Tone: Set the emotional register<br>• Audience: Define who this is for<br>• Response: Specify format (bullets, prose, code)",
                "## Common Prompt Mistakes",
                "• Being too vague ('Write about AI')<br>• Asking for everything at once<br>• Not specifying format<br>• Forgetting constraints (length, reading level)<br>• Not iterating on the first output",
                "## Practice Makes Perfect",
                "The best way to improve is to practice. Try the same prompt with different phrasings and compare results. Save your best prompts for reuse.",
            ],
        },
    ],
    "psychology": [
        {
            "title": "The Psychology of Habits: Why 1% Daily Improvement Matters",
            "category": "psychology",
            "tags": ["Psychology", "Habits", "Self-Improvement"],
            "body": [
                "## The Power of Small Wins",
                "Improving just 1% every day makes you 37x better after one year. The math is simple but the execution is hard — which is why most people never achieve their goals.",
                "## Why Habits Stick (or Don't)",
                "The habit loop: Cue → Craving → Response → Reward. Most people fail because they focus on the outcome (lose 20 pounds) instead of the system (exercise daily).",
                "## Atomic Habits in Practice",
                "• Make it obvious: Put your gym clothes next to your bed<br>• Make it attractive: Pair exercise with your favorite podcast<br>• Make it easy: Start with 2 minutes, not 30<br>• Make it satisfying: Track every completion visually",
                "## Start Your 1% Today",
                "Pick one tiny habit. Do it for 2 minutes. Repeat tomorrow. That's all it takes to start the compounding effect.",
            ],
        },
        {
            "title": "Stoicism for Modern Life: Ancient Wisdom That Still Works",
            "category": "psychology",
            "tags": ["Stoicism", "Philosophy", "Mental Health"],
            "body": [
                "## What Is Stoicism?",
                "An ancient Greek philosophy focused on controlling what you can and accepting what you cannot. It's experiencing a major revival among entrepreneurs and athletes.",
                "## The Dichotomy of Control",
                "Some things are up to you: your thoughts, actions, and opinions. Other things are not: the weather, others' opinions, the stock market. Focus only on the first category and you'll never feel powerless again.",
                "## Daily Stoic Practices",
                "• Morning meditation: Visualize challenges and prepare responses<br>• Throughout the day: Pause before reacting — ask 'Can I control this?'<br>• Evening journal: Review your actions — what went well, what could improve",
                "## Modern Applications",
                "Stoicism helps with: anxiety reduction, better decision-making, emotional resilience, focusing on what truly matters, and maintaining calm during market volatility.",
            ],
        },
        {
            "title": "Morning Routine Science: What the Research Says",
            "category": "psychology",
            "tags": ["Morning Routine", "Science", "Productivity"],
            "body": [
                "## The Science of Mornings",
                "How you spend the first hour of your day sets the tone for everything that follows. Research shows that willpower is highest in the morning and depletes throughout the day.",
                "## What Successful People Do Differently",
                "• No phone for the first 30-60 minutes (reduces cortisol spikes)<br>• Movement or exercise (increases BDNF for brain function)<br>• Goal-setting for the day (activates prefrontal cortex)<br>• Mindfulness or gratitude practice (reduces amygdala reactivity)",
                "## What to Avoid",
                "• Checking email first thing (puts you in reactive mode)<br>• News and social media (increases anxiety before work)<br>• Sugary breakfasts (causes energy crashes mid-morning)<br>• Decision-making on trivial matters (wastes finite willpower)",
                "## Build Your Routine Gradually",
                "Don't try to change everything at once. Add one new morning habit per week. Use a free habit tracker to stay consistent.",
            ],
        },
        {
            "title": "Overcoming Procrastination: The Science of Getting Started",
            "category": "psychology",
            "tags": ["Procrastination", "Psychology", "Focus"],
            "body": [
                "## Why We Procrastinate",
                "Procrastination isn't laziness — it's an emotional regulation problem. We avoid tasks that trigger negative emotions like anxiety, boredom, or self-doubt.",
                "## The 5-Second Rule",
                "Count backwards: 5-4-3-2-1-GO. This interrupts your brain's procrastination loop and activates your prefrontal cortex for action. The window of opportunity is only 5 seconds.",
                "## Reduce the Starting Friction",
                "• If a task takes <2 minutes, do it immediately<br>• Break big tasks into micro-steps with individual checkboxes<br>• Set a 5-minute timer and start — you can stop after 5 minutes<br>• Prepare your workspace the night before",
                "## Build Momentum",
                "Once you start, momentum carries you forward. Use the Pomodoro technique (25 min work, 5 min break) to maintain momentum throughout the day. Free online timers help you stay on track.",
            ],
        },
    ],
    "deals": [
        {
            "title": "Amazon Price Trackers: How to Never Pay Full Price Again",
            "category": "deals",
            "tags": ["Amazon", "Price Tracking", "Shopping"],
            "body": [
                "## The Problem with Amazon Pricing",
                "Amazon prices change constantly — sometimes multiple times per day. You might check a product and see $50, but miss the flash sale at $30 just two hours later.",
                "## How Automated Price Trackers Work",
                "Price monitoring services check product prices on a schedule (every hour, daily, etc.) and notify you when a price drops below your target. Set your target once and let automation do the rest.",
                "## What to Track",
                "• Electronics: Price drops can reach 40-50% during sales<br>• Books: New releases often drop within weeks<br>• Household items: Subscribe and save for regular purchases<br>• Gift items: Track before holiday price spikes",
                "## Never Miss a Deal Again",
                "Services like Deal Finder Pro automatically track thousands of Amazon products and send you notifications when prices hit their lowest levels. Stop checking manually — let automation save you money.",
            ],
        },
        {
            "title": "The Best Time to Buy on Amazon: A Data-Driven Guide",
            "category": "deals",
            "tags": ["Amazon", "Shopping", "Timing"],
            "body": [
                "## When Does Amazon Actually Have Sales?",
                "Here's what historical price data reveals about the best times to buy across different categories.",
                "## Best Timing by Category",
                "• Electronics: Prime Day (July), Black Friday (Nov), after Super Bowl<br>• Home & Kitchen: Spring cleaning season, January<br>• Fashion: End of season (Feb, Aug)<br>• Toys: October-December (but prices rise, buy early)",
                "## Day-of-Week Patterns",
                "Historical data shows that prices tend to drop mid-week (Tuesday-Thursday) and rise on weekends. Monday morning and Thursday evening are statistically the best times to find new deals.",
                "## Set and Forget with Automation",
                "Manual monitoring is inefficient. Automated deal trackers scan thousands of products 24/7 and notify you of price drops instantly — so you never miss a deal, even while sleeping.",
            ],
        },
    ],
}


def insert_cta(body_lines: list[str], category: str) -> list[str]:
    """Insert relevant product CTA mid-article."""
    cta = PRODUCT_CTAS.get(category)
    if not cta:
        return body_lines

    # Also add a second random CTA
    other_cats = [c for c in ALL_CATEGORIES if c != category]
    second = PRODUCT_CTAS.get(random.choice(other_cats))

    result = []
    for i, line in enumerate(body_lines):
        result.append(line)
        # Insert CTA after the middle of the article
        if i == len(body_lines) // 2:
            result.append(f'<div class="cta-box"><strong>{cta["text"]}</strong><br><a href="{cta["url"]}" target="_blank">{cta["name"]} — {cta["price"]}</a></div>')
        # Insert second CTA near the end
        if i == len(body_lines) - 2 and second:
            result.append(f'<div class="cta-box cta-secondary"><strong>{second["text"]}</strong><br><a href="{second["url"]}" target="_blank">{second["name"]} — {second["price"]}</a></div>')
    return result


def md_to_html(text: str) -> str:
    """Convert simple markdown-style text to HTML."""
    lines = text.split("\n")
    html_parts = []
    in_list = False
    list_type = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False; list_type = None
            continue
        if stripped.startswith("### "):
            if in_list: html_parts.append(f"</{list_type}>"); in_list = False; list_type = None
            html_parts.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith("## "):
            if in_list: html_parts.append(f"</{list_type}>"); in_list = False; list_type = None
            html_parts.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith("• ") or stripped.startswith("- ") or stripped.startswith("* "):
            txt = stripped.lstrip("•-* ")
            if not in_list or list_type != "ul":
                if in_list: html_parts.append(f"</{list_type}>")
                html_parts.append("<ul>"); in_list = True; list_type = "ul"
            html_parts.append(f"<li>{txt}</li>")
        elif len(stripped) > 2 and stripped[0].isdigit() and stripped[1:3] in (". ", ") "):
            txt = stripped.split(". ", 1)[1] if ". " in stripped else stripped.split(") ", 1)[1]
            if not in_list or list_type != "ol":
                if in_list: html_parts.append(f"</{list_type}>")
                html_parts.append("<ol>"); in_list = True; list_type = "ol"
            html_parts.append(f"<li>{txt}</li>")
        elif "<br>" in stripped or stripped.startswith("<"):
            if in_list: html_parts.append(f"</{list_type}>"); in_list = False; list_type = None
            html_parts.append(stripped)
        else:
            if in_list: html_parts.append(f"</{list_type}>"); in_list = False; list_type = None
            html_parts.append(f"<p>{stripped}</p>")
    if in_list:
        html_parts.append(f"</{list_type}>")
    return "\n".join(html_parts)


def generate_post_html(template: dict, date_str: str) -> tuple[str, str]:
    """Generate a full HTML post."""
    slug = template["title"].lower().replace(" ", "-").replace(":", "").replace("?", "")
    slug = "".join(c for c in slug if c.isalnum() or c in "-_")[:60]

    tags_html = " ".join(f'<span class="tag">{t}</span>' for t in template["tags"])
    body_with_cta = insert_cta(template["body"], template["category"])
    body_html = md_to_html("\n".join(body_with_cta))
    description = template["body"][1].replace("<br>", " ")[:160] if len(template["body"]) > 1 else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{template['title']}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{', '.join(template['tags'])}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://slashmantools.us/hermes-seo-farm/_posts/{slug}.html">
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
    .cta-box {{ background:linear-gradient(135deg,#1e293b,#334155); border:1px solid #475569; border-radius:12px; padding:20px; margin:25px 0; text-align:center; }}
    .cta-box strong {{ color:#f59e0b; display:block; margin-bottom:8px; }}
    .cta-box a {{ display:inline-block; background:#3b82f6; color:white; padding:8px 20px; border-radius:8px; text-decoration:none; font-weight:bold; margin-top:8px; }}
    .cta-box a:hover {{ background:#2563eb; }}
    .cta-secondary {{ background:linear-gradient(135deg,#1e293b,#0f172a); }}
    .cta-secondary a {{ background:#22c55e; }}
    .cta-secondary a:hover {{ background:#16a34a; }}
    a {{ color:#3b82f6; }}
    a:hover {{ color:#60a5fa; }}
    .back {{ display:inline-block; margin:20px 0; color:#64748b; text-decoration:none; font-size:0.9rem; }}
    .back:hover {{ color:#3b82f6; }}
    .share {{ margin:30px 0; text-align:center; }}
    .share a {{ margin:0 10px; }}
    footer {{ text-align:center; color:#475569; padding:30px 0; font-size:0.85rem; }}
</style>
</head>
<body>
    <a href="../index.html" class="back">&larr; Back to Blog</a>
    <h1>{template['title']}</h1>
    <div class="date">{date_str} · {template['category'].title()}</div>
    <div class="tags">{tags_html}</div>
{body_html}
    <div class="share">
        <p>Was this helpful? Share it!<br>
        <a href="https://twitter.com/intent/tweet?text=Check out: {template['title']}&url=https://slashmantools.us/hermes-seo-farm/_posts/{slug}.html" target="_blank">&#120143; Tweet</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u=https://slashmantools.us/hermes-seo-farm/_posts/{slug}.html" target="_blank">📘 Share</a>
        </p>
    </div>
    <footer>
        <p>Auto-generated by <a href="https://github.com/slashman413/hermes-seo-farm">hermes-seo-farm</a></p>
        <p style="margin-top:10px;"><small>Disclaimer: This content is for informational purposes only. Not financial or investment advice.</small></p>
    </footer>
</body>
</html>"""
    return html, slug


def generate_posts(count: int = 5) -> list[tuple[str, str, str]]:
    """Generate a set of SEO-optimized posts across categories."""
    posts = []
    categories = list(CONTENT_TEMPLATES.keys())
    random.shuffle(categories)
    today = datetime.now().strftime("%Y-%m-%d")

    used_templates = set()
    for category in categories:
        templates = [t for t in CONTENT_TEMPLATES[category] if t["title"] not in used_templates]
        if not templates:
            continue
        selected = random.sample(templates, min(1, len(templates)))
        for t in selected:
            if len(posts) < count:
                used_templates.add(t["title"])
                html_content, slug = generate_post_html(t, today)
                posts.append((html_content, slug, t["title"]))

    return posts


def build_site(posts: list[tuple[str, str, str]]):
    """Build the GitHub Pages site with all files."""
    docs_dir = BASE_DIR / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    posts_dir = docs_dir / "_posts"
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Write each post
    for html, slug, title in posts:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}.html"
        (posts_dir / filename).write_text(html, encoding="utf-8")
        print(f"  ✅ {filename}")

    # Build index with post links and site description
    post_links = ""
    for f in sorted(posts_dir.glob("*.html"), reverse=True):
        content = f.read_text(encoding="utf-8")
        t = ""
        ts = content.find("<title>")
        te = content.find("</title>")
        if ts >= 0: t = content[ts + 7:te]
        post_links += f'<li><a href="_posts/{f.name}">{t}</a> <span class="date">{f.name[:10]}</span></li>\n'

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Blog — Investing, Productivity, Tech, AI & Deals</title>
<meta name="description" content="Free articles on Taiwan stock investing, productivity tools, tech tutorials, psychology, AI tools, and Amazon deals. Updated daily.">
<meta name="keywords" content="Taiwan stocks, ETF, productivity, GitHub, AI tools, SEO, Amazon deals">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://slashmantools.us/hermes-seo-farm/">
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
    .cta {{ background:linear-gradient(135deg,#1e293b,#334155); border:1px solid #475569; border-radius:12px; padding:20px; text-align:center; margin:20px 0; }}
    .cta a {{ color:#f59e0b; font-weight:bold; }}
    footer {{ text-align:center; color:#475569; padding:20px; }}
</style>
</head>
<body>
    <h1>📝 Knowledge Blog</h1>
    <p class="subtitle">Taiwan Stocks · Productivity · Tech · Psychology · AI · Deals</p>
    <div class="cta">
        <strong>🎯 Daily articles auto-generated with AI</strong><br>
        <a href="https://ko-fi.com/s/a03f0a8e3b">Get the SEO Content Engine →</a>
    </div>
    <h2>Latest Articles</h2>
    <ul class="post-list">{post_links}</ul>
    <div class="cta">
        <strong>🔧 Need free tools?</strong><br>
        <a href="https://slashmantools.us/">20+ Free Online Tools → Calculators, PDF, QR, and more</a>
    </div>
    <footer>
        <p>Auto-generated daily by <a href="https://github.com/slashman413/hermes-seo-farm">hermes-seo-farm</a></p>
        <p><small>Disclosure: Some links on this site are affiliate links. We may earn a commission at no extra cost to you.</small></p>
    </footer>
</body>
</html>"""
    (docs_dir / "index.html").write_text(index_html, encoding="utf-8")
    (docs_dir / ".nojekyll").touch()
    print(f"✅ Generated index.html with {len(posts)} posts")


def main():
    print(f"📝 Generating SEO content for {datetime.now().strftime('%Y-%m-%d')}")
    posts = generate_posts(count=5)
    build_site(posts)
    print(f"✅ Done: {len(posts)} articles with product CTAs")


if __name__ == "__main__":
    main()
