#!/usr/bin/env python3
"""Retrieve and print words from an URL.

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
#    with urlopen('http://sixty-north.com/c/t.txt') as story:
    """Fetch a list of words from an URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
#    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)


# print(__name__)
if __name__ == '__main__':
#    words = fetch_words()
#    print_words(words)
    main(sys.argv[1])  # The 0th arg is the module filename
