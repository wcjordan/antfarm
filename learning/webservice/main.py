"""
Provides lightweight server for launching training runs
"""

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route('/start_training_run', methods=['POST'])
def start_training_run():
    return jsonify({'test':'testy'})


if __name__ == '__main__':
    app.run(debug=True)