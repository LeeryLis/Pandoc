from sys import stderr
from panflute import *

headlines = set()


def findBold(file):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))


def findDuplicateHeadlines(word, text):
    if type(word) == Header:
        headline = stringify(word)
        if headline in headlines:
            print("Some headers are the same", file=stderr)
        else:
            headlines.add(headline)


def headlinesBelowSecondUpperCase(word, text):
    if type(word) == Header and word.level > 2:
        return Header(Str(stringify(word).upper()), level=word.level)


if __name__ == "__main__":
    run_filters([findDuplicateHeadlines, headlinesBelowSecondUpperCase], prepare=findBold)