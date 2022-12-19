import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Hello,</h1> <h2>PassportPowell</h2>"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("ip", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
