import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

KEYWORDS = ["bim", "building information modeling", "digital construction"]

def fetch_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(strip=True)

            full_url = urljoin(url, href)

            combined_text = f"{text} {href}".lower()

            # filtro más flexible
            if any(keyword in combined_text for keyword in KEYWORDS):
                links.append({
                    "title": text if text else "No title",
                    "url": full_url
                })

        print(f"[DEBUG] {url} -> {len(links)} links encontrados")

        return links

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
