# Bitcoin Price Change Notifier 💰

This Python script scrapes the web every 5 seconds to get the current **BITCOIN price from Google Finance** 🌐.

## Features:** ✨
- Uses `requests` to fetch the HTML content from Google Finance.
- Employs `BeautifulSoup` to parse the HTML and extract the Bitcoin price.
- **Notifies the user if the price changes by more than $10.** 🔔
- Displays the timestamp of each price check and whether a significant change occurred. ⌚

## **How it Works:** ⚙️
1.  **Initialization:** The script sets the initial previous price to 0.
2.  **Web Scraping:** Inside an infinite loop:
    *   It sends a request to 'https://www.google.com/finance/quote/BTC-CAD' using `requests.get()`.
    *   It parses the HTML content using `BeautifulSoup` to find the specific `div` element containing the price.
    *   It extracts the price text, removes commas, and converts it to a float.

3.  **Price Comparison:**
    *   The `compare()` function checks if the absolute difference between the current price and the previous price is greater than $10.
    *   If it's the first comparison (previous price is 0), it skips the comparison.

4.  **Notification:**
    *   If the price change is significant, it prints a message with the timestamp indicating the change.
    *   Otherwise, it prints a message indicating no significant change.

5.  **Update Previous Price:**
    *   The previous price is updated with the current price for the next comparison.

6.  **Delay:** The script pauses for 5 seconds using `time.sleep(5)` before repeating the process.

## **Requirements:** 📋
*   Python 3
*   `requests` library
*   `beautifulsoup4` library

## **Installation:** 💾
1.  Install the required libraries using pip:
    ```bash
    pip install requests beautifulsoup4
    ```
2.  Save the script as `scrap.py`.

## **Usage:** 🚀
1.  Run the script from your terminal:
    ```bash
    python scrap.py
    ```
2.  The script will continuously monitor the Bitcoin price and notify you of significant changes.

## **Future Enhancements** 🚀
- Implement a logging system 📈
- Implement a more robust notification system: email, SMS, or push notifications to alert the user of price changes. 💌
- Allow the user to configure the price change threshold ⚙️
- Add support for other cryptocurrencies 💰
- Improve error handling ⚠️

## **Disclaimer:** ⚠️
This script is for educational purposes only. It should not be used for making financial decisions. The accuracy and reliability of the price data scraped from Google Finance are not guaranteed.

## Contributing 🤝
If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

