from forex_python.converter import CurrencyRates

def main():
    # Create an instance of CurrencyRates
    currency = CurrencyRates()
    
    try:
        # Prompt the user to enter the amount and currencies
        amount = float(input("Enter the amount: "))
        from_currency = input('Enter the from currency (e.g., USD): ').upper()
        to_currency = input('Enter the to currency (e.g., EUR): ').upper()
        
        # Print the conversion details
        print(f"Converting {amount} {from_currency} to {to_currency}...")
        
        # Perform the currency conversion
        result = currency.convert(from_currency, to_currency, amount)
        
        # Print the conversion result
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the amount.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
