import os
from flask import Flask, render_template
from datetime import datetime
from flask import Flask, redirect, request, session, url_for



app = Flask(__name__)
app.secret_key = "randomstring123"
messages =[]

def add_messages(username, message):
    """Add Message to the message list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format( now, username,message))

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


@app.route('/chatlogin')
def chatlogin():
    return render_template("chatlogin.html")



@app.route('/chatapp')
def chatapp():
    return render_template("chatapp.html")



@app.route("/", methods=["GET", "POST"])
def home():
    """ Main Page with instruction"""
    if request.method == "POST":
        return redirect(url_for("chatapp"))  



@app.route('/<username>')
def user(username):
    """ Display chat Message"""
    return "<h1>Welcome,{0}</h1>{1}".format(username, get_all_messages())



@app.route('/<username>/<message>')
def send_message(username,message):
    """ Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == "__main__":
       app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)