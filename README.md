# NaNoGenMo 2015

I wrote this for [NaNoGenMo 2015](https://github.com/dariusk/NaNoGenMo-2015/).  It doesn't "generate" a novel so much as mangle an existing one, but it was fun.  Given a text, this code can convert it through a series of languages and back to the original.

This uses the Yandex Translator API, so an API key is required.  You can set that up here: https://tech.yandex.com/keys/get/?service=trnsl

According to the API docs, you can do 1,000,000 characters per day but not more than 10,000,000 per month.  So if your text is 200,000 characters, and you convert it through 4 languages and back to English (or back to the initial language), you will have used up your translation quota for the day.

Also according to the docs, the max size of a request is 10 kB, but I got "large request" errors around 8 kB, so the documentation may be out of date.  You can configure the size of the request when instantiating the Telgame class, which is what makes the API requests.  For example, this:

```python
tg = Telgame(4000)
```

will chunk the text into at most 4000 characters per request, always breaking on a word boundary.

A full list of supported languages and their codes is in the [languages supported file](languages-supported.md).
