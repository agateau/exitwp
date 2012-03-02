#!/usr/bin/env python
import os
import re
import sys
from optparse import OptionParser

USAGE="%prog <arg1> <arg2>..."

"""
Example of link to replace:

[![](http://agateau.files.wordpress.com/2012/01/bird-eye-view.png?w=300)](http://agateau.files.wordpress.com/2012/01/bird-eye-view.png)

"""

MAIN_RX = re.compile(
    r"\[\s*!"
    + r"\[([^]]*)\]" # Possible title
    + r"\(([^)]+)\)" # img url
    + r"\s*\]"
    + r"\(([^)]+)\)" # href url
    )

SIZE_RX = re.compile(r"\?w=(\d+)$")

SITE_URL = "http://agateau.files.wordpress.com"

IMAGE_EXTS = [".jpeg", ".jpg", ".png", ".gif"]

def repl(match):
    title, img, href = match.groups()

    if img.startswith(SITE_URL):
        img = img[len(SITE_URL):]
    if href.startswith(SITE_URL):
        href = href[len(SITE_URL):]

    if img == href:
        # A full image (no link)
        return "![%s](%s)" % (title, href)

    title = title.replace('"', r"'")

    if img.startswith("/") and href.startswith("/"):
        size_match = SIZE_RX.search(img)
        if size_match is not None:
            # A dynamic thumbnail linking to a full image
            size = size_match.group(1)
            return '{%% thumbimg title="%(title)s" href="%(href)s" size="%(size)s" %%}' % locals()

        if os.path.splitext(href)[1].lower() in IMAGE_EXTS:
            # A home-made thumbnail linking to a full image
            return '{%% thumbimg title="%(title)s" src="%(img)s" href="%(href)s" %%}' % locals()

    # An image linking to some other content
    if img.startswith("/"):
        # Make sure img does not have any query parameter, Jekyll does not support them
        img = img.split("?")[0]
    return "[![%(title)s](%(img)s)](%(href)s)" % locals()


class App(object):
    def __init__(self):
        self.dry_run = True
        self.in_place = False

    def run(self, name):
        txt = open(name).read()
        if self.dry_run:
            print "#", name
            for match in MAIN_RX.finditer(txt):
                print match.groups()
                print "=>", repl(match)
                print
        else:
            print >>sys.stderr, "#", name
            txt = MAIN_RX.sub(repl, txt)
            if self.in_place:
                fl = open(name, "w")
            else:
                fl = sys.stdout
            fl.write(txt)


def main():
    parser = OptionParser(usage=USAGE)

    # Add a boolean option stored in options.verbose.
    parser.add_option("--dry-run",
                      action="store_true", dest="dry_run", default=False,
                      help="Simulate replacement")

    # Add a boolean option stored in options.verbose.
    parser.add_option("-i", "--in-place",
                      action="store_true", dest="in_place", default=False,
                      help="In place. Default to printing to stdout")

    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.error("Missing args")

    app = App()
    app.dry_run = options.dry_run
    app.in_place = options.in_place

    for arg in args:
        app.run(arg)

    return 0


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
