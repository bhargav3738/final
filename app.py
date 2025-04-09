from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>DevOps Showcase - Bhargav</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
          body {{
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: #fff;
          }}
          .glass-card {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
            backdrop-filter: blur(6px);
          }}
          .quote {{
            font-style: italic;
            font-size: 1.1rem;
            margin-top: 20px;
            color: #ddd;
          }}
        </style>
      </head>
      <body class="d-flex justify-content-center align-items-center vh-100">
        <div class="container text-center glass-card">
          <h1 class="display-4 mb-3">🚀 Bhargav Nimbalkar</h1>
          <p class="lead">DevOps Test #2 deployed on <strong>AWS ECS Fargate</strong></p>
          <span class="badge bg-success fs-5 mb-3">Status: LIVE</span>
          <p>Current Server Time: <strong>{current_time}</strong></p>
          <a href="/" class="btn btn-outline-light mt-3">🔄 Refresh</a>
          <div class="quote mt-4">"Success usually comes to those who are too busy to be looking for it."</div>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
