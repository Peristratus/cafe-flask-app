import os
from flask import Flask, render_template
from datetime import datetime
from flask import Flask, redirect, request, session, url_for


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_message(username, message):
    """Add Message to the message list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


def get_all_messages():
    """"get all of the messages and separate using a br"""
    return "<br>".join(messages)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/products')
def products():
    return render_template("products.html")


@app.route('/chat')
def chat():
    return render_template("chat.html")  


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/chatlogin', methods=["GET", "POST"])
def chatlogin():
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return render_template("chatapp.html", username=session["username"], chat_messages = messages)
        
    return render_template("chatlogin.html", username = "Untitled") 


@app.route('/chatapp')
def chatapp():
    username = session["username"]

    if request.method == "POST":
        message = request.form["message"]
        add_message(username, message)
        print(messages)
        return render_template("chatapp.html", username = username, chat_messages = messages)

    return render_template("chatapp.html", username = username, chat_messages = messages)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)