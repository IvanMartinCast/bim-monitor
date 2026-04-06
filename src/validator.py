def is_official(url):
    whitelist = [
        ".gov", ".gob", ".gov.uk", ".gc.ca",
        "buildingsmart", "iso.org", "europa.eu"
    ]
    return any(w in url.lower() for w in whitelist)


def is_bim_relevant(title):
    keywords = ["bim", "building information modeling", "iso 19650"]
    return any(k in title.lower() for k in keywords)
