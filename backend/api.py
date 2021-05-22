import flask
from roleta import Roleta

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getPoints', methods=['GET'])
def getPoints():
    roleta = Roleta()
    point = {
        'value': roleta.pontuacaoRodada()
    }
    return point

app.run()