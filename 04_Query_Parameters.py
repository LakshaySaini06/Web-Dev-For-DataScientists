from flask import Flask , request

app = Flask(__name__)

@app.route('/predict')
def predict():
    x = request.args.get('x' , default=0)
    y = request.args.get('y', default=10)
    return f" x = {x} and y = {y}"

if __name__ == '__main__' :
    app.run(debug= True)

# handling missing values

# x = request.args.get('x' , default=0)

# if 'x' in request.args:
#     x = request.args['x']