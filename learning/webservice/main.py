"""
Provides lightweight server for launching training runs
"""
import subprocess

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route('/start_training_run', methods=['POST'])
def start_training_run():
    proc = subprocess.Popen(["python", "runners/tictactoe.py"], stdout=subprocess.PIPE)
    output = proc.stdout.read()

    return jsonify({'test':output.decode("utf-8")})


if __name__ == '__main__':
    app.run(debug=True)