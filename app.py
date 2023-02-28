from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World tuhsar!</h1>"

@app.route("/Hello1World")
def hello_world1():
    return "<h1>Hello, World tuhsar1!</h1>"

@app.route("/Hello2World")
def hello_world2():
    return "<h1>Hello, World tuhsar2!</h1>"

@app.route("/test")
def test():
    a=5+6

    return "this is my function to run app{}".format(a)

@app.route("/test2")
def test2():
    data=request.args.get('x')
    return 'this is my data input from url {}'.format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")
