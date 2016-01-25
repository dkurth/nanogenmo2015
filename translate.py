from telgame import Telgame
import re
import sys

if __name__ == "__main__":
    tg = Telgame(4000)
    filename = 'hamlet.txt'

    langs = ['ja',  # Japanese
            'cy',  # Welsh
            'sw',  # Swahili
            'he',  # Yiddish
            'en']  # English

    with open(filename, 'rb') as fh:
        content = fh.read()
    content = content.decode('utf-8')

    for i in range(1, len(langs)):
        conv = "{}-{}".format(langs[i-1], langs[i])
        print("\n" + conv)

        content = tg.convert(content, conv)

        with open("{}.{}.txt".format(filename, conv), 'w', encoding='utf-8') as fh:
            for str in content:
                fh.write(str)

    print("Done.")
