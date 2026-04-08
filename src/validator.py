def is_official(url):
    official_domains = [
        ".gov", ".gob", ".gov.uk", ".eu",
        "buildingsmart", "iso.org"
    ]
    return any(domain in url.lower() for domain in official_domains)


def is_bim_relevant(title):
    keywords = [
        "bim",
        "iso 19650",
        "building information",
        "digital construction"
    ]
    return any(k in title.lower() for k in keywords)
