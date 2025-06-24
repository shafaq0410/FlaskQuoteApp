

from flask import Flask, render_template, request, redirect, url_for
from random import randint

app = Flask(__name__)

# Route to show the name form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("hello", name=name))
    return render_template("index.html")

# Route to display the quote page with user's name
@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' — John Louis von Neumann",
        "'Computer science is no more about computers than astronomy is about telescopes.' — Edsger Dijkstra",
        "'To understand recursion you must first understand recursion..' — Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' — Unknown",
        "'Mathematics is the key and door to the sciences.' — Galileo Galilei",
        "'Not everyone will understand your journey. That's fine. It's not their journey to make sense of. It's yours.' — Unknown",
        "'The limits of my language mean the limits of my world.' — Ludwig Wittgenstein",
        "'Programs must be written for people to read, and only incidentally for machines to execute.' — Harold Abelson",
        "'Simplicity is the soul of efficiency.' — Austin Freeman",
        "'First, solve the problem. Then, write the code.' — John Johnson",
        "'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.' — Martin Fowler",
        "'Before software can be reusable it first has to be usable.' — Ralph Johnson",
        "'The best way to get a project done faster is to start sooner.' — Jim Highsmith",
        "'In order to be irreplaceable, one must always be different.' — Coco Chanel",
        "'Experience is the name everyone gives to their mistakes.' — Oscar Wilde",
        "'It's not a bug. It's an undocumented feature!' — Anonymous",
        "'Talk is cheap. Show me the code.' — Linus Torvalds",
        "'Good code is its own best documentation.' — Steve McConnell",
        "'Code is like humor. When you have to explain it, it’s bad.' — Cory House",
        "'Innovation distinguishes between a leader and a follower.' — Steve Jobs"
    ]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]
    return render_template("test.html", name=name, quote=quote)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

