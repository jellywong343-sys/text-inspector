# Text Inspector

[绠€浣撲腑鏂嘳(README.zh-CN.md)

Analyze text files and report lines, characters, terms, and frequent words with JSON export.

## Highlights

- Python standard library only; no runtime dependencies.
- Command-line interface and automated tests included.
- Safe defaults and clear output.
- Windows, macOS, and Linux; Python 3.10+.

## Installation

```bash
git clone https://github.com/jellywong343-sys/text-inspector.git
cd text-inspector
python -m pip install -e .
```

Replace `jellywong343-sys` with your GitHub username.

## Usage

```bash
text-inspect notes.md
text-inspect notes.md article.txt --top 15 --json report.json
```

Run `text-inspect --help` to see every option.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
text-inspector/
鈹溾攢鈹€ src/text_inspector/
鈹溾攢鈹€ tests/
鈹溾攢鈹€ README.md
鈹溾攢鈹€ README.zh-CN.md
鈹溾攢鈹€ pyproject.toml
鈹斺攢鈹€ LICENSE
```

## Safety

Review command output before applying changes to important files. Keep backups of irreplaceable data.

## License

MIT




