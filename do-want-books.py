#!/usr/bin/env python
"""
A wrapper to the do-we-want-it API at want.archive.org to determine if a book is needed.

Desired functionality:

  o Read a single line of input from the user, either an ISBN or the title of a book.
  o Take the ISBN and plug into the API and return the results in a relatively pretty format.
  o If it's a book title, search ISBNDB for results. Ask for user confirmation. (Maybe make
    a UI and download the book cover image to help confirm?) Return the results.
  o Read from a file or ISBNs and/or book titles, confirming each result with the user.
  o Have the ability to output to a prettified file so the user can reference what books
    they would like to send the Archive.
"""

import sys
import argparse
import textwrap

def main():
    description="""\
    Look up a book at archive.org to see if they need it for their collection.
    """
    parser = argparse.ArgumentParser(description=textwrap.dedent(description))
#group = parser.add_mutually_exclusive_group()
#group.add_argument("-i", "--isbn", dest="isbn", help="Look up by ISBN (10 or 13 digit format)", action="store")
#group.add_argument("-t", "--title", dest="title", help="Look up by title (must be in double quotes)", action="store")
    parser.add_argument("-i", "--isbn", dest="isbn", help="Look up by ISBN (10 or 13 digit format)", action="store")
    parser.add_argument("-t", "--title", dest="title", help="Look up by title (must be in double quotes)", action="store")
    args = parser.parse_args()
# make the user give you either an ISBN or a title - empty argument should return the usage statement 
    if len(sys.argv)==1:
        parser.print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
