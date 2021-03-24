from newspaper import Article
import nltk
from colorama import init, Fore, Back, Style


def extract_info(link):
    nltk.download('punkt')

    url = link
    article = Article(url)
    article.download()
    article.parse()

    print(Fore.GREEN + "\n[Title]: " + Fore.RESET + f"{article.title}")
    print(Fore.GREEN + "[Publish date]: " + Fore.RESET + f"{article.publish_date}")

    article.nlp()
    print(Fore.GREEN + f"\n[A few summary lines]\n")
    print(Fore.RESET + article.summary)

    print(Fore.GREEN + f"\n[Article Keywords:]\n" + Fore.RESET)
    print(article.keywords)

if __name__ == '__main__':
    init(convert=True)
    url = input("Paste link here: ")
    extract_info(url)