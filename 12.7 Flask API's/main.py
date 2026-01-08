from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
        "Harry": 56,
        "Rohan": 67,
        "Aakash": 78,
        "Shubham": 92,
        "Reena": 67,
    }
    values = [1 , marks, 100]
    return jsonify(values)

app.run(debug = True)
