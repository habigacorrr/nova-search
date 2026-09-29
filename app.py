
from flask import Flask, request, render_template_string
from urllib.parse import quote_plus

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#09090f">

<title>NOVA — Search Beyond</title>

<style>
:root {
    --bg: #09090f;
    --text: #f5f5ff;
    --muted: #9292a8;
    --surface: #171722;
    --border: #29293a;
    --accent: #9585ff;
}

body.light {
    --bg: #f7f7fc;
    --text: #191925;
    --muted: #737386;
    --surface: #ffffff;
    --border: #dedeea;
    --accent: #6653db;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: var(--bg);
    color: var(--text);
    font-family: Inter, system-ui, sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    transition: background .3s, color .3s;
}

header {
    display: flex;
    justify-content: flex-end;
    padding: 22px 28px;
}

header button {
    background: transparent;
    border: none;
    color: var(--text);
    font-size: 14px;
    cursor: pointer;
}

main {
    width: 100%;
    max-width: 760px;
    margin: auto;
    padding: 35px 22px 80px;
    text-align: center;
}

.logo {
    font-size: clamp(58px, 14vw, 100px);
    font-weight: 800;
    letter-spacing: -7px;
    line-height: 1.2;
    background: linear-gradient(
        120deg, #a99aff, #6b8dff, #dc8dff
    );
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: appear .8s ease;
}

.subtitle {
    color: var(--muted);
    margin: 15px 0 35px;
    font-size: 15px;
}

.search-box {
    display: flex;
    align-items: center;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 7px 9px 7px 20px;
    transition: .25s;
    box-shadow: 0 12px 40px rgba(0,0,0,.15);
}

.search-box:focus-within {
    border-color: var(--accent);
    box-shadow: 0 0 0 4px rgba(149,133,255,.12);
}

.search-box input {
    flex: 1;
    min-width: 0;
    background: transparent;
    border: none;
    outline: none;
    color: var(--text);
    font-size: 16px;
    padding: 13px 0;
}

.search-box input::placeholder {
    color: var(--muted);
}

.search-box button {
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 13px 19px;
    font-weight: 600;
    cursor: pointer;
    transition: .2s;
}

.search-box button:hover {
    filter: brightness(1.12);
    transform: translateY(-1px);
}

.shortcuts {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 25px;
}

.shortcut {
    border: 1px solid var(--border);
    color: var(--muted);
    background: var(--surface);
    padding: 10px 16px;
    border-radius: 30px;
    cursor: pointer;
    font-size: 13px;
    transition: .2s;
}

.shortcut:hover {
    color: var(--accent);
    border-color: var(--accent);
    transform: translateY(-2px);
}

.info {
    margin-top: 55px;
    color: var(--muted);
    font-size: 13px;
    line-height: 1.8;
}

footer {
    text-align: center;
    padding: 22px;
    color: var(--muted);
    font-size: 12px;
    border-top: 1px solid var(--border);
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media(max-width: 480px) {
    header { padding: 18px; }
    main { padding-left: 16px; padding-right: 16px; }
    .logo { letter-spacing: -4px; }
    .search-box { border-radius: 15px; padding-left: 15px; }
    .search-box button { padding: 12px 14px; }
}
</style>
</head>

<body>

<header>
    <button onclick="toggleTheme()" id="themeButton">
        ☀️ Light mode
    </button>
</header>

<main>

    <div class="logo">NOVA</div>

    <p class="subtitle">
        Search beyond what you know.
    </p>

    <form class="search-box" action="/search" method="GET">
        <input
            type="search"
            name="q"
            id="query"
            placeholder="Ask anything..."
            autocomplete="off"
            aria-label="Search the internet"
            required
        >

        <button type="submit">Search ↗</button>
    </form>

    <div class="shortcuts">
        <button class="shortcut"
            onclick="searchFor('Artificial intelligence')">
            ✦ AI
        </button>

        <button class="shortcut"
            onclick="searchFor('Technology news')">
            ◈ Technology
        </button>

        <button class="shortcut"
            onclick="searchFor('Science discoveries')">
            ◎ Science
        </button>

        <button class="shortcut"
            onclick="searchFor('Interesting facts')">
            ✧ Discover
        </button>
    </div>

    <div class="info">
        <p>One search. Endless possibilities.</p>
        <p>Powered by DuckDuckGo search.</p>
    </div>

</main>

<footer>
    NOVA Search © 2026 · Built for curious minds.
</footer>

<script>
const input = document.getElementById("query");
const themeButton = document.getElementById("themeButton");

function searchFor(query) {
    input.value = query;
    input.form.submit();
}

function toggleTheme() {
    const isLight = document.body.classList.toggle("light");

    themeButton.textContent = isLight
        ? "🌙 Dark mode"
        : "☀️ Light mode";

    try {
        localStorage.setItem(
            "nova-theme",
            isLight ? "light" : "dark"
        );
    } catch (error) {}
}

try {
    if (localStorage.getItem("nova-theme") === "light") {
        document.body.classList.add("light");
        themeButton.textContent = "🌙 Dark mode";
    }
} catch (error) {}
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip()

    if not query:
        return render_template_string(HTML), 400

    search_url = (
        "https://duckduckgo.com/?q="
        + quote_plus(query)
    )

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>Searching — NOVA</title>
        <style>
            body {{
                background: #09090f;
                color: #f5f5ff;
                font-family: system-ui, sans-serif;
                display: grid;
                place-items: center;
                min-height: 100vh;
                text-align: center;
                padding: 20px;
            }}
            h1 {{ color: #9585ff; }}
            a {{ color: #a99aff; }}
        </style>
    </head>
    <body>
        <div>
            <h1>NOVA</h1>
            <p>Searching for: {query}</p>
            <p>Redirecting to search results...</p>
            <p>
                <a href="{search_url}">
                    Click here if you are not redirected.
                </a>
            </p>
        </div>
        <script>
            window.location.replace({search_url!r});
        </script>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "online",
        "application": "NOVA Search",
        "version": "1.0"
    }


import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=False
    )