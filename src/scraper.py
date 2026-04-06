import requests
from bs4 import BeautifulSoup

def fetch_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(strip=True)

            if "bim" in text.lower() or "bim" in href.lower():
                links.append({
                    "title": text,
                    "url": href if href.startswith("http") else url + href
                })

        return links

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
