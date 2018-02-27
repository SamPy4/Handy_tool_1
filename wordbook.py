import requests
from lxml import html

def fetch(wordLink, word):
    print(wordLink)
    newLink = []
    try:
        page = requests.get(wordLink)
    except requests.exceptions.ConnectionError:
        print("Fetcher couldn't fetch: No internet connection")
        return

    tree = html.fromstring(page.content)

    trans = []
    for i in range(1, 11):
        try:
            tX = '/html/body/div[1]/div[5]/table[1]/tbody/tr[3]/td[2]/a/text()'
                 '/html/body/div[1]/div[5]/table[1]/tbody/tr[3]/td[2]/a'
            trans.append(tree.xpath(tX))
        except IndexError:
            break
    print(trans)
    return trans

word = input().strip().lower()
wordLink = 'http://www.sanakirja.org/search.php?q={}&l=17&l2=3?s=t'.format(word)

translations = fetch(wordLink, word)

for t in translations:
    print(t, "\n")
