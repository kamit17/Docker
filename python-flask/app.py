from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>The Lord of the Rings Trilogy</title>
      <style>
        body {
          margin: 0;
          padding: 0;
          height: 100vh;
          background-image: url('https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=1500&q=80');
          background-size: cover;
          background-position: center;
          background-repeat: no-repeat;
          color: #f9d57f;
          font-family: 'Georgia', serif;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        .title {
          background: rgba(0, 0, 0, 0.6);
          padding: 40px 60px;
          border-radius: 20px;
          text-align: center;
          box-shadow: 0 0 20px #49340a;
        }
        h1 {
          font-size: 2.5em;
          margin-bottom: 20px;
          letter-spacing: 2px;
        }
        ul {
          list-style: none;
          padding: 0;
          margin: 0;
          font-size: 1.5em;
        }
        li {
          margin: 10px 0;
        }
        a {
          color: #f9d57f;
          text-decoration: none;
          transition: color 0.3s ease;
        }
        a:hover {
          color: #ffd965;
          text-decoration: underline;
        }
      </style>
    </head>
    <body>
      <div class="title">
        <h1>The Lord of the Rings</h1>
        <ul>
          <li><a href="https://www.imdb.com/title/tt0120737/" target="_blank" rel="noopener noreferrer">The Fellowship of the Ring</a></li>
          <li><a href="https://www.imdb.com/title/tt0167261/" target="_blank" rel="noopener noreferrer">The Two Towers</a></li>
          <li><a href="https://www.imdb.com/title/tt0167260/" target="_blank" rel="noopener noreferrer">The Return of the King</a></li>
        </ul>
      </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
