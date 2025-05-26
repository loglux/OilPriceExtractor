# OilPriceExtractor

**OilPriceExtractor** is a Python script that uses Selenium to extract home heating oil prices for various litre options from [deandrews.co.uk](https://deandrews.co.uk/product/home-heating-oil/).

## 🧰 Features

- Automates interaction with the volume dropdown on the product page
- Extracts the corresponding price for each litre option
- Supports headless browser mode for silent execution
- Outputs a simple dictionary of `{litres: price}` pairs

## 📦 Requirements

- Python 3.7+
- Google Chrome installed
- [ChromeDriver](https://chromedriver.chromium.org/) matching your Chrome version in `PATH`

Install required Python packages:

```bash
pip install selenium
```

## 🚀 Usage

```bash
python main.py
```

Sample output:

```
500 litres: £345.67
900 litres: £610.23
1200 litres: £810.45
```

You can modify the URL or enable full browser mode by editing the script:

```python
extractor = OilPriceExtractor('https://deandrews.co.uk/product/home-heating-oil/', headless=False)
```

## 📄 Notes

- The script assumes the page structure remains stable.
- The `<select>` element must have the ID `litres`.
- Price is extracted from `.woocommerce-Price-amount.amount`.

## 🧹 Clean Exit

Don't forget to close the browser instance using `extractor.close()` after scraping.

## 📄 License

MIT License — use freely, attribution appreciated.

## 🤝 Contributions

Improvements are welcome! Fork the repo and submit a pull request.
