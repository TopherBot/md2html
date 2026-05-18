# md2html

A tiny Python CLI that converts a Markdown file to HTML.

## Install

```bash
pip install markdown
```

## Usage

```bash
# Convert a file
python md2html.py input.md > output.html

# Or pipe from stdin
cat input.md | python md2html.py > output.html
```

## Features

- **Zero‑dependency** besides the `markdown` package.
- Reads from a file argument or from **stdin** when no argument is given.
- Writes the resulting HTML to **stdout**, so it can be chained.

## License

MIT
