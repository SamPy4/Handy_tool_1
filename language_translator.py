import requests
from lxml import html

class language_translator():
    def __init__(self):
        self.lang_1 = 3     # 3  = eng
        self.lang_2 = 17    # 17 = fin

        """ Declaring language dictionary """
        self.langs = {"e" : 3,
                      "s" : 15,
                      "f" : 17}


    def fetch_words(self, word):
        """ Returns either list of words or None indicating that it didn't find translations """
        url = 'http://www.sanakirja.org/search.php?q={word}&l={l1}&l2={l2}'.format(word=word,
                                                                                   l1  =self.lang_1,
                                                                                   l2  =self.lang_2)
        try:
            page = requests.get(url)
        except requests.exceptions.ConnectionError:
            print("No internet connection")
            return False

        tree = html.fromstring(page.content)
        firstWord = '/html/body/div[1]/div[5]/table[1]/tbody/tr[3]/td[2]/a/text()'
        firstWord = '/html/body/div[1]/div[5]/table[1]/tbody/tr[1]/th[1]/text()'
                    # '/html/body/div[1]/div[5]/table[1]/tbody/tr[3]/td[2]/a'
        fw = tree.xpath(firstWord)

        return fw

    def get_translation(self, word, l1, l2):
        """ This will fetch the translation """
        """ This function is called from outside """
        try:
            self.lang_1 = self.langs[l1]    # Updates the global var
            self.lang_2 = self.langs[l2]    # Updates the global var
        except:
            return False

        word = str(word).strip().lower()
        return self.fetch_words(word)

if __name__ == "__main__":
    lt = language_translator()
    tr = lt.get_translation("fool", "e", "f")
    print(tr)
    exit()
