from flask import Flask, render_template, request
import yfinance as yf
import requests  # You need this for the custom session

# Create the Flask app
app = Flask(__name__)

# Set up the custom User-Agent for yfinance to avoid 429 errors
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None
    error = None

    # Handle form submission
    if request.method == "POST":
        symbol = request.form.get("symbol").upper().strip()

        try:
            ticker = yf.Ticker(symbol, session=session)
            hist = ticker.history(period="5d")
            print(f"History Data for {symbol}:\n", hist)  # Add this line

            if hist.empty:
                error = f"No data found for symbol: {symbol}"
            else:
                stock_data = {
                    "symbol": symbol,
                    "history": hist.reset_index().to_dict("records")
                }

        except Exception as e:
            error = str(e)
            print("Error occurred:", error)

    return render_template("index.html", stock=stock_data, error=error)

# Start the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
