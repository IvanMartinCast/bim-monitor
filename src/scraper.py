import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

KEYWORDS = [
    "bim",
    "iso 19650",
    "building information modeling",
    "digital construction",
    "bim standard",
    "bim guide"
]

def fetch_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(strip=True)

            full_url = urljoin(url, href)
            combined = f"{text} {href}".lower()

            if any(k in combined for k in KEYWORDS):
                if full_url.startswith("http"):
                    links.append({
                        "title": text if text else "Documento BIM",
                        "url": full_url
                    })

        print(f"🔎 {url} → {len(links)} posibles documentos BIM")

        return links

    except Exception as e:
        print(f"Error en {url}: {e}")
        return []
