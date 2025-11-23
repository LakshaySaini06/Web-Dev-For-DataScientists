from flask import Flask , render_template , jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    # some ML Model
    data = {"Output" : 69  , "Accuracy" : 98}
    return jsonify(data),200

app.run(debug=True)