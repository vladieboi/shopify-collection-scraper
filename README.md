# What is this?

This is a simple script that scrapes any Shopify website and creates a file containing the website's collections. The script provides all collection data available in the `/colletions.json` endpoint (with one exception - the collection description). This might also serve as a great learning resource into making requests.

# Contribute

Feel free to fork this script and modify it, or open a pull request to improve it.

# Install

1. Make sure you have Python3 and Pip installed. Check using `python --version` and `pip --version`
2. Clone repo using `git clone https://github.com/vladieboi/shopify-collection-scraper/` (or download it)
3. Navigate to download folder repo using `cd path/to/download/folder`
4. Install required packages using `pip install -r requirements.txt`
5. Run the script using `python scraper.py`

---

# Arguments

| Argument            | Type | Default | Values |
|---------------------|------|---------|--------|
| `--domain`          | Str  |         |        |
| `--output`          | List | `csv`   | `csv`  |

## Example command

```py
python3 scrape.py --domain eu.kith.com
```
