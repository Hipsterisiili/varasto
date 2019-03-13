from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Essi Esimerkki"

kerayspaikat = [1, 2, 3, 4]

tuotteet = []
tuotteet.append(Item("Makaroni"))
tuotteet.append(Item("Cola"))
tuotteet.append(Item("Ketsuppi"))
tuotteet.append(Item("vessapaperi"))
  
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, kerayspaikat=kerayspaikat, tuotteet=tuotteet)

if __name__ == "__main__":
    app.run(debug=True)
