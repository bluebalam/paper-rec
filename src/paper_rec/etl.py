import json
import feedparser
import nltk

from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

feeds = ["http://export.arxiv.org/rss/cs.AI",
         "http://export.arxiv.org/rss/cs.CL",
         "http://export.arxiv.org/rss/cs.CV",
         "http://export.arxiv.org/rss/cs.IR",
         "http://export.arxiv.org/rss/cs.LG",
         "http://export.arxiv.org/rss/stat.ML",
         ]


def get_title(e):
    return e.title.split("(arXiv:")[0].strip()


def get_summary(e):
    return BeautifulSoup(e.summary, "lxml").text.replace('\n', " ").strip()


def get_authors(e):
    return BeautifulSoup(e.author, "lxml").text.strip()


def clean_text(txt):
    return BeautifulSoup(txt, "lxml").text.replace('\n', " ")


def process_feeds(feeds):
    entries = []

    for feed_url in feeds:
        print(f"processing {feed_url}")
        feed = feedparser.parse(feed_url)
        entries.extend(feed['entries'])

    papers = [
        {
            "id": e.id,
            "title": get_title(e),
            "authors": get_authors(e),
            "abstract": get_summary(e),
            "sentences": get_sentences(e)
        } for e in entries
    ]
    return papers


def dump_jsonl(records, fname):
    with open(fname, "w") as fout:
        for r in records:
            fout.write(json.dumps(r))
            fout.write("\n")


def get_sentences(e):
    # title as first sentence
    title = get_title(e)
    # sentences from summary
    summary = clean_text(e.summary)
    sentences = sent_tokenize(summary)
    return [title] + sentences
