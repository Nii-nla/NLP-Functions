from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia"""
    print(f"Searching Wikipedia for: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize Wikipedia"""
    print(f"Summarizing Wikipedia for: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """gets text blob object and returns"""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and return phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
