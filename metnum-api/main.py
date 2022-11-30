from flask import Flask
from flask import jsonify

# Importamos todas las ecuaciones
from equations.secante import secante


app = Flask(__name__)


@app.route('/api/equations', methods=['GET'])
def get_equations():
    response = {'resultado': secante()}
    return jsonify(response)


@app.route('/api/equations', methods=['POST'])
def get_equations():
    response = {'resultado': 'No tenemos de momento'}
    return jsonify(response)


@app.route('/api/equations', methods=['DELETE'])
def get_equations():
    response = {'resultado': 'No tenemos de momento'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
