"""
Provides lightweight server for launching training runs
"""
import http
import subprocess

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route('/start_training_run', methods=['POST'])
def start_training_run():
    subprocess.Popen(
        ["python", "runners/tictactoe.py",
         str(request.json['id'])],
        shell=False)
    return '', http.HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run(debug=True)
