from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Lakshay"
    language = "Python"
    luckynos = [29,31, 25 , 26 , 10 , 29 ]
    footer = "<p> All rights reserved  | Copyright 2025  </p>"
    return render_template("index.html", name = name , lang = language , lucky = luckynos , footer = footer)

app.run(debug=True)

