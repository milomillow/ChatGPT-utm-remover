#  Removedor de ?utm_source=chatgpt.com em Python
# Este script remove URLs que contem o parametro do ChatGPT
# Criado por: MiloMilow
# Licença: MIT

# Removedor de ?utm_source=chatgpt.com com suporte a idiomas (PT/EN)
# Criado por: MiloMilow
# Licença: MIT

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def remove_utm_source_chatgpt(url):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if 'utm_source' in query and 'chatgpt.com' in query['utm_source']:
        del query['utm_source']
    new_query = urlencode(query, doseq=True)
    new_url = urlunparse(parsed._replace(query=new_query))
    return new_url

def main():
    # Escolha do idioma
    idioma = ''
    while idioma not in ('pt', 'en'):
        idioma = input("Escolha o idioma / Choose language (pt/en): ").lower()

    # Mensagens em pt e en
    msgs = {
        'pt': {
            'entrada': "Digite a URL (ou 'sair' para finalizar): ",
            'saida': "URL limpa: ",
            'sair': 'sair'
        },
        'en': {
            'entrada': "Enter the URL (or 'exit' to finish): ",
            'saida': "Clean URL: ",
            'sair': 'exit'
        }
    }

    while True:
        url = input(msgs[idioma]['entrada'])
        if url.lower() == msgs[idioma]['sair']:
            break
        limpa = remove_utm_source_chatgpt(url)
        print(msgs[idioma]['saida'], limpa)

if __name__ == "__main__":
    main()
