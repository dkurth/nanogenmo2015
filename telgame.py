import requests
import urllib
import json
import sys
import re

'''
    For GET requests, the maximum size of the request string is 10 kB.
    Can do 1,000,000 characters per day but not more than 10,000,000 per month.
'''

class Telgame:
    def __init__(self, chunk_size=8000, max_len=None):
        self.baseUrl = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.apiKey = 'ENTER API KEY HERE'
        self.chunk_size = chunk_size
        self.max_len = max_len
        self.verbose = True

    def convert(self, content, lang):
        translated_content = ""

        chunks = self.word_chunks(content, self.chunk_size)

        if self.verbose:
            print("Breaking the content into {} chunks of size <= {}".format(len(chunks), self.chunk_size))

        for counter, chunk in enumerate(chunks):
            if counter == 0 or counter % 20 == 0:
                print('.')
            else:
                print('.', end="")
            sys.stdout.flush()

            if self.max_len is not None and (len(translated_content) + len(chunk)) >= self.max_len:
                break

            params = {
                'key': self.apiKey,
                'text': chunk,
                'lang': lang
            }
            r = requests.post(self.baseUrl, params)
            data = r.json()
            if 'text' in data:
                for str in data['text']:
                    translated_content += str
            else:
                print("The chunk size was: {}".format(len(chunk)))
                print("The response was: {}".format(data))

        return translated_content

    def word_chunks(self, string, max_length):
        # breaks string into chunks with len(chunk) <= max_length, and always ends at a word boundary
        return [c for c in re.split('(.{,'+str(max_length)+'})\\b', string, flags=re.DOTALL) if c != '']