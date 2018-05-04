import requests
from lxml import html

def parseInput(input):
    return

def fetch(word):
    word = str(word)
    word = word.strip().lower()

    wordLink = 'http://www.thesaurus.com/browse/{}?s=t'.format(word)
    newLink = []
    try:
        page = requests.get(wordLink)
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return None

    tree = html.fromstring(page.content)
    wordTypeX  = '/html/body/div[1]/div/div/div/div/div/div[2]/section[1]/div/span/em/text()'
    descX      = '/html/body/div[1]/div/div/div/div/div/div[2]/section[1]/div/span/strong/text()'
               # '/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[2]/strong'
               #OLD XPATH descX      = '/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[2]/strong/text()'
               #OLD XPATH wordTypeX  = '/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[2]/em/text()'

    # synonymsX = '/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[3]/div/ul[1]'
    # synonymsX = '/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[3]/div/ul[1]/li[1]/a/@href'

    try:
        wordType = tree.xpath(wordTypeX)[0]
        desc     = tree.xpath(descX)[0]
    except IndexError:
        print("Word not found!!!")
        return False
    except:
        print("Some other error")
        raise

    synonyms = []


    for j in range(1, 100):
        try:
            for i in range(1, 100):
                try:
                    # synonymsX = '/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[3]/div/ul[{}]/li[{}]/a/span/text()'.format(j, i)
                    synonymsX = '/html/body/div[1]/div/div/div/div/div/div[2]/section[{}]/ul/li[{}]/span/a/text()'.format(j, i)
                    synonyms.append(tree.xpath(synonymsX)[0].strip())
                except IndexError:
                    break
        except:
            break

    return wordType, desc, synonyms

def getData(input):
    return



if __name__ == "__main__":
    word = input().strip().lower()
    wordLink = 'http://www.thesaurus.com/browse/{}?s=t'.format(word)

    wordType, desc, synonyms = fetch(word)


    print("\n\n{word}\n    {type};  {desc}".format(word=word, type=wordType, desc=desc))

    print()

    for s in synonyms:
        print(s, "\n")
