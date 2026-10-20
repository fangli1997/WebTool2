
# WebTool 🔎

A lightweight Python website status checker that checks
whether a website is reachable.

## Features

- Check website HTTP status codes
- Detect connection errors and timeouts
- Supports URLs with or without `https://`
- Interactive command-line interface
- No external dependencies

## Requirements

- Python 3.8+

## Usage

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/webtool.git
cd webtool
```

Run the script:

```bash
python main.py
```

Enter a website URL when prompted:

```text
========================================
       WEBTOOL - URL CHECKER
========================================

Enter website URL (or 'exit'): example.com

Checking: https://example.com
----------------------------------------
Status: 200
Result: Website is reachable
```

Type `exit` to quit.

## Project Structure

```text
webtool/
├── main.py
└── README.md
```

## License

MIT
