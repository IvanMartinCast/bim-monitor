import json
from scraper import fetch_links
from validator import is_official, is_bim_relevant
from parser import parse_document
from updater import update_data

def run():
    with open("config/countries.json") as f:
        config = json.load(f)

    results = []

    for country, data in config.items():
        for region in data["regions"]:
            for source in data["sources"]:

                links = fetch_links(source)

                for link in links:
                    if is_official(link["url"]) and is_bim_relevant(link["title"]):
                        parsed = parse_document(link, country, region)
                        results.append(parsed)

    print("RESULTADOS:", len(results))
    update_data(results)

if __name__ == "__main__":
    run()
