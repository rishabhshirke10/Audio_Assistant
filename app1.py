from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import time

app = Flask(__name__)


def run_assistant():
    try:
        subprocess.run(
            ["python", "AS.py"], check=True
        )  # Replace 'your_python_file.py' with the filename of your Python code
    except subprocess.CalledProcessError as e:
        print(e)
        return str(e)


@app.route("/")
def home():
    return render_template("appwindow1.html")


@app.route("/start_assistant", methods=["POST"])
def start_assistant():
    output_messages = []

    def send_message(message):
        output_messages.append(message)

    t = threading.Thread(target=run_assistant, args=(), daemon=True)
    t.start()

    while t.is_alive():
        time.sleep(1)
        if output_messages:
            yield f"data: {output_messages.pop(0)}\n\n"

    yield "data: Assistant finished\n\n"


if __name__ == "__main__":
    app.run(debug=True)
