# Stock Market Analyzer

This is a simple Flask web app that allows users to input a stock ticker symbol and view recent stock price data using the Yahoo Finance API via the `yfinance` library.

## Features

- Accepts stock ticker input (e.g., AAPL, TSLA, MSFT)
- Fetches and displays the last 5 days of stock data
- Shows Open, Close, High, Low, and Volume
- Simple web interface using Flask
- Dockerized for easy deployment

## Project Structure

```
stock-analyzer/
├── app.py               # Main Flask app
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container configuration
├── templates/
│   └── index.html       # HTML frontend
└── static/              # Optional static files (CSS, JS)
```

## Getting Started (Local)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/stock-analyzer.git
   cd stock-analyzer
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:
   ```bash
   python app.py
   ```

5. **Open in your browser**:
   Visit `http://localhost:5000`

## Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t stock-analyzer .
   ```

2. **Run the container**:
   ```bash
   docker run -d -p 8000:5000 stock-analyzer
   ```

3. **Access the app**:
   Open `http://localhost:8000` in your browser.

## Notes

- Make sure your machine has internet access.
- If Yahoo Finance blocks requests (Error 429), try again later or reduce request frequency.
- This app uses only the `yfinance.Ticker(...).history()` method to avoid rate-limited endpoints.

## License

This project is open source and available under the MIT License.