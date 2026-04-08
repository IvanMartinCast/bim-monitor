def is_official(url):
    official_domains = [
        ".gov", ".gob", ".gov.uk", ".eu",
        "buildingsmart", "iso.org",
        "gov", "minister", "public"
    ]
    return any(d in url.lower() for d in official_domains)


def is_bim_relevant(title):
    keywords = [
        "bim",
        "iso 19650",
        "building information modeling",
        "construction digital",
        "standard",
        "regulation"
    ]
    return any(k in title.lower() for k in keywords)
