# Currency_Converter

# Currency Converter

This is a simple Python command-line application that converts an amount from one currency to another using real-time exchange rates. The application uses the `forex-python` library to fetch the latest exchange rates.

## Features

- Convert an amount from one currency to another in real-time.
- Supports all major currencies.
- User-friendly command-line interface.

## Prerequisites

- Python 3.x installed on your system.
- The `forex-python` library, which can be installed via `pip`.

## Installation

1. Clone the repository or download the project files:

    ```bash
    git clone https://github.com/your-username/currency-converter.git
    cd currency-converter
    ```

2. Install the required Python packages:

    ```bash
    pip install forex-python
    ```

## Usage

1. Run the script using Python:

    ```bash
    python main.py
    ```

2. Enter the amount you wish to convert when prompted.

3. Specify the currency you are converting from (e.g., USD) and the currency you are converting to (e.g., EUR). The currency codes should follow the standard ISO 4217 format (e.g., USD, EUR, GBP, etc.).

4. The script will display the converted amount.

### Example

```bash
Enter the amount: 100
Enter the from currency (e.g., USD): USD
Enter the to currency (e.g., EUR): EUR
Converting 100.0 USD to EUR...
100.0 USD is equal to 92.34 EUR
