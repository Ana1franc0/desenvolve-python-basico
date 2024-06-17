def extrair_dominio(url):
    return url[4:-4]

def main():
    urls = [
        "www.google.com&quot",
        "www.gmail.com&quot",
        "www.github.com&quot",
        "www.reddit.com&quot",
        "www.yahoo.com&quot"
    ]

    dominios = [extrair_dominio(url) for url in urls]
    print("Domínios:", dominios)
    