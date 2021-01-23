import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")  


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/chatapp")
def chatapp():
    return "To Sender a message use / USERNAME / MESSAGE"



@app.route('/<username>')
def user(username):
    return "Hi  "  +   username



@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)