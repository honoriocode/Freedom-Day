#Code by HonorioCode

from flask import Flask

app = Flask(__name__)

import datetime
now = datetime.date.today()
slavedays = datetime.date (2022,5,28)
freedomday = datetime.date (2022,5,29)

@app.route("/")
def home():
    if now <= slavedays:
        return "Você ainda é um escravo"
    elif now == freedomday:
        return "Hoje é o dia que você vai começar a produzir para si"
    else:
        return "Você está no período em que não está trabalhando pro governo. Aproveite"

if __name__ == "__main__":
    app.run()  