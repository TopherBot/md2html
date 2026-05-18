#!/usr/bin/env python3
"""md2html: Convert Markdown to HTML in a single script.

Usage:
  python md2html.py [input.md] > output.html
If no input file is given, the script reads from stdin.
"""
import sys

try:
    import markdown
except ImportError:
    sys.stderr.write("Please install the 'markdown' package: pip install markdown\n")
    sys.exit(1)


def main():
    # Determine source of markdown text
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except OSError as e:
            sys.stderr.write(f"Error reading {path}: {e}\n")
            sys.exit(1)
    else:
        text = sys.stdin.read()

    # Convert and output
    html = markdown.markdown(text)
    sys.stdout.write(html)


if __name__ == "__main__":
    main()
